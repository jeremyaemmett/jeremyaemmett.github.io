# Spacecraft observation geometry (in-prep, Python)

#### _[&larr; Main](index.md)_

---

#### _[Source code](maven1.py)_

Ungraduate work in 2012-2014 involved prediction of future observational geometries of the IUVS (Imaging UltraViolet Spectrograph) instrument aboard the MAVEN mars orbiter, to identify optimal time windows for observations of aurorae during the instrument's apoapsis (full-disk) scan phases. Software was developed in an IDL (Interactive Data Language) framework. 
Spacecrat position/velocity and instrument pointing geometry were derived from the NASA SPICE toolkit:
https://naif.jpl.nasa.gov/pub/naif/pds/pds4/maven/maven_spice/document/spiceds_v001.html

Scan footprints were represented on cylindrical planetary maps displaying day/night regions and magnetic field topology.

![mavenexample](https://github.com/user-attachments/assets/fda03388-def1-4cd9-b068-cbdd80ea286e)

A Python re-make is in development, also utilizing the NASA SPICE toolkit, and improved with modularized kernel downloading, more sophisticated visualization capabilities, and improved code documentation.

![apoapsis_scans2](https://github.com/user-attachments/assets/14104b63-4a01-481d-9650-3505e6bacac2)
