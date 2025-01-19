# Involute Gear

**[involute_gear.py](involute_gear.py)**

#### _[&larr; Main](index.md)_

A simulation and tracing method for designing an involute spur gear, as described by Lcamtuf.coredump.cs.

---
![involute_gear_steps](https://github.com/user-attachments/assets/03c3e843-4c55-4504-bb1c-051f6ccfbed6)
---
The user specifies tooth number, tooth width, and tooth contact angle.
1. A linear gear slides across edge of a circular gear with circumference 'C'. A a constant rotation rate is desired for the circular gear. This is achieved if the tooth carves out a "V"-shaped profile, as shown in cyan, and is drawn by relating the position of the tooth along the rack 'D' to the rotation angle 'A' of the circle: A = D * 360 / C. The resultant 'involute' pattern is duplicated according to the desired number of teeth. The 'points' of the teeth are 'blunted' by overplotting an addendum circle.
2. The shape of interest (the traced spur gear) is isolated from the rest of the image with an interior flood-fill algorithm.
3. The spur gear's edge is traced with a Canny edge detection algorithm.
4. Image coordinates are converted back to physical coordinates to allow the edge point coordinates to be plotted at the correct scale.
