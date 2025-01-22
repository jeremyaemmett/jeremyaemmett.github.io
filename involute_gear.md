# Involute Gear

A Python implementation of a simulation-tracing method for designing an involute spur gear, as described by [Lcamtuf.coredump.cs.](https://lcamtuf.coredump.cx/gcnc/ch6/)

Source Code:
[involute_gear.py](https://github.com/jeremyaemmett/jeremyaemmett.github.io/blob/main/involute_gear.py)

#### _[&larr; Main](index.md)_

---
![involute_gear_steps](https://github.com/user-attachments/assets/03c3e843-4c55-4504-bb1c-051f6ccfbed6)
---
The user specifies tooth number, tooth width, and tooth contact angle.

1. A linear gear slides across edge of a circular gear with circumference 'C'. The linear gear teeth have a prescribed trapezoidal profile, but can assume any closed shape. A constant rotation rate is desired for the circular gear. This is achieved if the tooth carves out a "V"-shaped profile, as shown in cyan. The tooth carving profile is drawn by relating the position of the tooth 'D' along the linear gear, to the rotation angle 'A' of the circle: A = D * 360 / C. The pattern is duplicated according to the desired number of teeth. The 'points' of the resulting teeth are 'blunted' by overplotting a calculated addendum circle. The plot is saved as a modifiable image in pixel coordinates.

2. The gear shape is isolated from the rest of the image with an interior flood-fill algorithm and pixel value filter.

3. The spur gear's edge is traced with a Canny edge detection algorithm.

4. Pixel coordinates are converted back to physical coordinates, to allow the edge points to be plotted at the correct scale and with respect to any specified origin.
