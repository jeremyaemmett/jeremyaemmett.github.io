# Spacecraft observation geometry (in-prep, Python)

#### _[&larr; Main](index.md)_

---

Ungraduate work in 2012-2014 involved predicting future observational geometries of the IUVS (Imaging UltraViolet Spectrograph) instrument aboard the MAVEN mars orbiter, to identify optimal time windows for observations of aurorae during the instrument's apoapsis (full-disk) scan phases. Software was developed in an IDL (Interactive Data Language) framework. 
Spacecraft position/velocity and instrument pointing geometry were derived from the NASA SPICE toolkit:
https://naif.jpl.nasa.gov/pub/naif/pds/pds4/maven/maven_spice/document/spiceds_v001.html

Scan footprints were represented on cylindrical planetary maps displaying spacecraft ground tracks, spectrograph slit footprints, and magnetic field topology. Strong contrast between magnetic field open/closed boundaries was interpreted as a proxy for auroral activity potential, with nightside observations favored.

![mavenexample](https://github.com/user-attachments/assets/fda03388-def1-4cd9-b068-cbdd80ea286e)

_IDL-generated cylindrical Mars map displaying a select apoapsis scan phase superimposed on magnetic field topology._

A Python re-make is in development, with modularized kernel downloading tools, more sophisticated visualization capabilities, and improved code documentation. This robust code architecture is universally applicable to any spacecraft/instrument provided that SPICE kernels exist and provide coverage for the time range of interest. 
#### _[Source code](maven1.py)_

![apoapsis_scans2](https://github.com/user-attachments/assets/14104b63-4a01-481d-9650-3505e6bacac2)
_Two views of an identical apoapsis scan phase. Left: Near face-on view of the apoapsis-facing side of Mars. Right: Near face-on view of the MAVEN spacecraft's highly elliptical orbital plane. Slit footprints are represented as red projections on the planet's surface. Orange rays indicate the spacecraft position during the apoapsis scan phase as well as lines-of-sight emanating from the IUVS slit midpoint. "Hourglasses" result from the slit's left-to-right sweep superimposed on the spacecraft's orbital motion. Left-to-right and top-to-bottom scan sweeps occur with respect to the instrument's default pointing direction, MAVEN's orbital periapsis vector._

![temp2](https://github.com/user-attachments/assets/2c7b3741-9790-4101-bde1-57017995da36)

_Animation of a partial apoapsis scan phase, with planet rotation, MAVEN's retrograde/sun-synchronous orbit, and right-left/bottom-up scan "sweeps"._
