# Involute Gear

**[involute_gear.py](involute_gear.py)**

#### _[&larr; Main](index.md)_

A simulation and tracing method for designing an involute spur gear, as described by Lcamtuf.coredump.cs.

---
![involute_gear_steps](https://github.com/user-attachments/assets/03c3e843-4c55-4504-bb1c-051f6ccfbed6)
The user specifies tooth number and width.
1. A toothed rack slides parallel to the edge of a circular gear with circumference 'C' with the aim of driving a constant rotation rate for the circular gear. This is achieved if the tooth carves out a "V"-shaped profile, as shown in cyan, and is drawn by relating the position of the tooth along the rack 'D' to the rotation angle 'A' of the circle (which is equivalent to the rotation angle of the tooth, from the perspective of an observer on the gear surface): A = D * 360 / C. The resultant pattern is duplicated around the circle, according to the desired number of spur gear teeth. The 'points' of the spur gear teeth are 'blunted' by overplotting an addendum circle.
2. The shape of interest (the traced spur gear) is isolated from the rest of the image with an interior flood-fill algorithm.
3. The spur gear's edge is traced with a Canny edge detection algorithm.
4. Image coordinates are converted back to physical coordinates to allow the edge point coordinates to be plotted at the correct scale.
