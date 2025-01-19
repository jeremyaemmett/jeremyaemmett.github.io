from skimage.segmentation import flood, flood_fill
from matplotlib.image import imread
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math
import cv2

def rotate(origin, point, angle):
    # Rotate a 2D vector [px, py] around the point [ox, oy]

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy

### User-specified parameters
tooth_count = 12.0
tooth_width = 1.0
p_angle = 18.0 # Pitch angle (degrees)
user_path = 'C:/Users/Jeremy/Desktop/'

# Calculated parameters defining the effective gear diameter (pitch) and tooth height/depth
c_pitch = tooth_width * 2.0 * tooth_count
r_pitch = (c_pitch / np.pi) / 2.0
addendum = tooth_width * 2.0 / np.pi

# Configure the simulation tracing plot window
fig = plt.figure(figsize=(8, 8), frameon=False)
fig.tight_layout()
ax = fig.add_subplot(111)
ax.set_box_aspect(1)
ax.tick_params(axis='x', direction='in', pad = -15)
ax.tick_params(axis='y', direction='in', pad=-15)
ax.set_axis_off()
ax.set_xlim([-2.2*r_pitch, 2.2*r_pitch])
ax.set_ylim([-2.2*r_pitch, 2.2*r_pitch])

# Truncate the tooth by the addendum
theta = np.linspace(0, 2.0*np.pi, 180)
ax.plot((r_pitch + addendum)*np.cos(theta), (r_pitch + addendum)*np.sin(theta), color = 'black', linestyle = '-')

for a in np.arange(0.0, 360.0, 360.0 / tooth_count):

    for d in np.arange(-5.0, 5.0, 0.5):

        # The angle of the gear with respect to the y-axis, when the gear-driving tooth is at distance d from the y-axis
        angle = math.radians(d * (360.0 / c_pitch))

        # Vertex positions of the tooth profile at its calculated angle and distance
        # Upper sides
        x1_r, y1_r = tooth_width / 2.0, r_pitch
        x1_l, y1_l = -x1_r, y1_r
        x2a_r, y2a_r = x1_r + 0.2 * r_pitch * np.cos(math.radians(90.0 - p_angle)), \
                       y1_r + 0.2 * r_pitch * np.sin(math.radians(90.0 - p_angle))
        x2a_l, y2a_l = -x2a_r, y2a_r
        v1, v4 = (x2a_l + d, y2a_l), (x2a_r + d, y2a_r)
        # Lower sides
        trunc_side_length = (1.05 * addendum) / np.sin(math.radians(90.0 - p_angle))
        x2b_r, y2b_r = x1_r + trunc_side_length * np.cos(math.radians(270.0 - p_angle)), \
                       y1_r + trunc_side_length * np.sin(math.radians(270.0 - p_angle))
        x2b_l, y2b_l = -x2b_r, y2b_r
        # Base
        v2, v3 = (x2b_l + d, y2b_l), (x2b_r + d, y2b_r)

        # Consider which tooth is being traced. Teeth are separated by angle a.
        v1, v2 = rotate((0.0, 0.0), v1, angle + math.radians(a)), rotate((0.0, 0.0), v2, angle + math.radians(a))
        v3, v4 = rotate((0.0, 0.0), v3, angle + math.radians(a)), rotate((0.0, 0.0), v4, angle + math.radians(a))

        # Plot the tooth outline
        norm = (10.0 - abs(d))/10.0
        col = 'black' # Default tooth tracing color
        if a == 0.0: col = 'teal' # First tooth tracing color
        ax.plot([v1[0], v2[0], v3[0], v4[0]], [v1[1], v2[1], v3[1], v4[1]], linestyle='-', c=col, alpha=max(0.05, norm))

plt.savefig(user_path + 'involute_gear_tracing.jpg', dpi=100, bbox_inches='tight', pad_inches=0)

## Image Processing
# Get the image
image_rgb = imread(user_path + 'involute_gear_tracing.jpg')
image = imread(user_path + 'involute_gear_tracing.jpg')[:,:,0]
# Fill the gear interior and clean up outlying lines
midx, midy = int(np.shape(image)[1]/2), int(np.shape(image)[0]/2)
filled_image = flood_fill(image, (midx, midy), 200, tolerance=200)
filled_image[filled_image != 200] = 255
# Perform edge detection, record edge coordinates
edges = cv2.Canny(filled_image, 100, 255)
indices = np.where(edges != [0])
coordinates = zip(indices[0], indices[1])
# Convert image coordinates back to true coordinates
x_coords_true, y_coords_true = indices[0] - midx, indices[1] - midy
x_coords_true = 2.0 * x_coords_true * 2.2 * r_pitch / np.shape(image)[1]
y_coords_true = 2.0 * y_coords_true * 2.2 * r_pitch / np.shape(image)[0]

## Subplots showing algorithm steps
# Configure plot window
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
fig.subplots_adjust(wspace=0, hspace=0.3)
# Simulation tracing
ax[0, 0].imshow(image_rgb)
ax[0, 0].set_title('1. Simulation Tracing')
# Interior fill
ax[0, 1].imshow(filled_image, cmap=plt.cm.gray)
ax[0, 1].set_title('2. Interior Flood Fill')
# Canny edge detection
ax[1, 0].imshow(edges, cmap=plt.cm.gray_r)
ax[1, 0].set_title('3. Canny Edge Detection')
# Re-scaled gear outline, with relevant radii
ax[1, 1].set_box_aspect(1)
ax[1, 1].scatter(x_coords_true, y_coords_true, c = 'black', marker = '.', s = 0.1)
theta = np.linspace(0, 2.0 * np.pi, 180)
ax[1, 1].plot((r_pitch - 1.05 * addendum)*np.cos(theta), (r_pitch - 1.05 * addendum)*np.sin(theta), color = 'blue', linestyle = '--', alpha = 0.3)
ax[1, 1].plot(r_pitch*np.cos(theta), r_pitch*np.sin(theta), color = 'red', linestyle = '--', alpha = 0.3)
ax[1, 1].plot((r_pitch + addendum)*np.cos(theta), (r_pitch + addendum)*np.sin(theta), color = 'green', linestyle = '--', alpha = 0.3)
ax[1, 1].set_title('4. Re-scaled Edge Coordinates')

plt.savefig(user_path + 'involute_gear_steps.jpg', dpi=100, bbox_inches='tight', pad_inches=0)
