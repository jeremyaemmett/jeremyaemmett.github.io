from typing import Callable, Iterator, Iterable, Optional, Tuple, Union, Sequence
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import spiceypy as spice
import numpy as np
import requests
import ctypes
import math
import cv2
import os

def radius(B2):

    # Longitudinal radius of Mars and distance below/above the equator, at a given latitude B2 (given in degrees)
    B2 = math.radians(B2)
    R2 = 3389.5 * math.cos(B2)
    Z2 = 3389.5 * math.sin(B2)

    return R2, Z2

def rotation_matrix(axis, theta):

    # Rotation matrix associated with counterclockwise rotation about the given axis by theta radians
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d

    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

def mpl_sphere(image_file):

    # Read the map image
    img = plt.imread(image_file)

    # Define a grid matching the map size, subsample along with pixels
    theta = np.linspace(0, np.pi, img.shape[0])
    phi = np.linspace(0, 2*np.pi, img.shape[1])

    # Keep 180 points along theta and phi
    count = 360
    theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
    phi_inds = np.linspace(0, img.shape[1] - 1, count).round().astype(int)
    theta = theta[theta_inds]
    phi = phi[phi_inds]
    img = img[np.ix_(theta_inds, phi_inds)]

    # Plot an isometric 3D sphere with the overlayed map texture
    theta,phi = np.meshgrid(theta, phi)
    R = 3389.5
    x = R * np.sin(theta) * np.cos(phi)
    y = R * np.sin(theta) * np.sin(phi)
    z = R * np.cos(theta)
    ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1, alpha = 1.0, zorder = 0, shade = False) # we've already pruned ourselves
    ax.axis('scaled')

def haversine(Olat,Olon, Dlat,Dlon):

    # Distance between two given lat/lon coordinates

    radius = 6371.  # km

    d_lat = np.radians(Dlat - Olat)
    d_lon = np.radians(Dlon - Olon)
    a = (np.sin(d_lat / 2.) * np.sin(d_lat / 2.) +
         np.cos(np.radians(Olat)) * np.cos(np.radians(Dlat)) *
         np.sin(d_lon / 2.) * np.sin(d_lon / 2.))
    c = 2. * np.arctan2(np.sqrt(a), np.sqrt(1. - a))
    d = radius * c
    return d

# Calculate a grid of lat/lon distances from the sub-solar point, for day/night determination
solar_lat, solar_lon = 20.0, -105.0
lats, lons = np.linspace(-90.0, 90.0, 100), np.linspace(-180.0, 180.0, 100)
lats_1, lons_1 = np.meshgrid(lats, lons)
test = haversine(solar_lat, solar_lon, lats_1, lons_1)

# Load the original map image
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
image_file = 'C:/Users/Jeremy/Desktop/mars_cylindrical.jpg'
img = cv2.imread(image_file)
height, width = img.shape[0], img.shape[1]

# Save a new map image with overlayed day/night regions
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
lons_1 = width * lons_1 / (np.max(lons_1) - np.min(lons_1)) + width/2.0
lats_1 = height * lats_1 / (np.max(lats_1) - np.min(lats_1)) + height/2.0
ax.contourf(lons_1, lats_1, np.flipud(test), cmap = 'gist_gray', levels=1, alpha = 0.5)
ax.set_xlim([0.0, 0.999*width])
plt.savefig('C:/Users/Jeremy/Desktop/temp.jpg', dpi=400, bbox_inches='tight', pad_inches=0)

mode = 'download'
mode = 'test'

# Read the meta kernel file to get the list of kernels to download/load
filename = 'maven_meta.txt'
with open(filename) as file:
    lines = [line.rstrip().split("'")[1] for line in file if 'maven_kernels' in line]

if mode == 'download': # Download the kernels, if needed

    main_url = 'https://naif.jpl.nasa.gov/pub/naif/MAVEN/kernels/'
    for line in lines:
        folder, file = line.split('/')[1], line.split('/')[2]
        url = main_url + folder + '/' + file
        response = requests.get(url)
        file_Path = 'maven_kernels/' + folder + '/' + file
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
            print('File downloaded successfully')

# Load all of the kernels listed in the meta kernal file
cwd = os.getcwd()
spice.furnsh(cwd + "\maven_meta.txt")

# Date range for positions, velocities, and times
utc = ['Jun 5, 2022, 1:00:00', 'Jun 5, 2022, 4:38:00']

# Convert start and end times to ET (seconds after the J2000 epoch)
etOne, etTwo = spice.str2et(utc[0]), spice.str2et(utc[1])

# Get [n_steps] times between the start and end ETs
n_steps = 4000
times = [x*(etTwo-etOne)/n_steps + etOne for x in range(n_steps)]

# Get position coordinates (I, J, K = inertial Mars-centric coordinates)
positions, lightTimes = spice.spkpos('Maven', times, 'J2000', 'NONE', 'MARS BARYCENTER')
positions = positions.T # positions is shaped (4000, 3), transpose to (3, 4000) for easier indexing

# Get state vectors
state_vectors, lightTimes = spice.spkezr('Maven', times, 'J2000', 'NONE', 'MARS BARYCENTER')

# Initial position and velocity for orbital element determination
r0, v0 = state_vectors[0][0:3], state_vectors[0][3:]

# Angular momentum vector, h
h = np.cross(r0, v0)

# Node vector, n
n = np.array([-h[1], h[0], 0.0])

# Mars' GM parameter
mu_mars = 0.042828e6 #km^3/s^2

# Eccentricity vector
e = (1.0 / mu_mars) * ( (np.linalg.norm(v0)**2.0 - (mu_mars / np.linalg.norm(r0))) * r0 - (np.dot(r0, v0)) * v0)

# Periapsis vector
p = (h**2.0) / mu_mars

# Vector perpindicular to the orbital plane, +90 deg from periapsis (instrument rotation axis 1)
axis1 = np.cross(e, h)
# Vector parallel to the orbital plane, +90 deg from periapsis (instrument rotation axis 2)
axis2 = h

# Clean up the kernels
spice.kclear()

# Configure plot window
fig = plt.figure(figsize=(9, 9))
ax  = fig.add_subplot(111, projection='3d', computed_zorder=False)
ax.plot(positions[0], positions[1], positions[2], alpha = 0.5)
ax.set_xlim([-5000, 5000])
ax.set_ylim([-5000, 5000])
ax.set_zlim([-5000, 5000])
ax.set_box_aspect([-1.0, -1.0, -1.0])

# Slit center line-of-sight defaults to be parallel to the periapsis vector
look_vector_0 = e / np.linalg.norm(e)
look_vector_0 = 10000.0 * look_vector_0 / np.linalg.norm(look_vector_0)

# Angular length of the slit
slit_angles = np.linspace(-7.0, 7.0, 29)

# Initial left-to-right sweep angle of the slit center
sweep_angle = -20.0

# Main graphical/computational time loop
for p in range(0, positions.shape[1]):

    # Position at time p
    positn = np.array([positions[0, p], positions[1, p], positions[2, p]])

    # Left-to-right sweep angle of the slit center at time p
    sweep_angle = sweep_angle + 0.15
    look_vector = np.dot(rotation_matrix(axis1, math.radians(sweep_angle)), look_vector_0)
    if sweep_angle > 20.0: sweep_angle = -20.0

    # Draw at every nth timestep to save memory
    if p%10 == 0:

        for i in range(0, len(slit_angles)):

            # Draw the slit lines-of-sight from bottom to top with respect to the slit center line-of-sight
            look_vector2 = np.dot(rotation_matrix(axis2, math.radians(slit_angles[i])), look_vector)
            # Check for planet intersection
            test = spice.surfpt(positn, look_vector2, 3389.5, 3389.5, 3389.5)

            if test[-1]:

                # Plot the footprint if intersection = True
                ax.plot(test[0][0], test[0][1], test[0][2], color='red', marker='.', markersize = 0.8)
                if slit_angles[i] == 0.0:
                    ax.plot([test[0][0], positn[0]], [test[0][1], positn[1]], [test[0][2], positn[2]], color='orange', linestyle='-', alpha = 0.3)

# Plot the equator, or other latitudes of choice
for lat in range(-90, 90, 5):

    rad, z2 = radius(lat)
    theta = np.linspace(0, 2 * np.pi, 201)
    x = rad * np.cos(theta)
    y = rad * np.sin(theta)
    z = 0.0 * x + z2
    #if lat == 0: ax.plot(x, y, z, color='limegreen', alpha = 0.3)

# Overlay the map image on the ellipsoid
mpl_sphere('C:/Users/Jeremy/Desktop/temp.jpg')

# Set the initial viewing angle
ax.view_init(300, 30)
ax.view_init(0, 30)

# Make a black background
ax.set_axis_off()
ax.set_facecolor('black')

plt.show()

