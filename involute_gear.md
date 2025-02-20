# Involute Gear

A Python implementation of a simulation-tracing method for designing an involute spur gear, as described by [Lcamtuf.coredump.cs.](https://lcamtuf.coredump.cx/gcnc/ch6/)

Source Code:
[involute_gear.py](https://github.com/jeremyaemmett/jeremyaemmett.github.io/blob/main/involute_gear.py)

#### _[&larr; Main](index.md)_

---
![involute_gear_steps](https://github.com/user-attachments/assets/03c3e843-4c55-4504-bb1c-051f6ccfbed6)
---
The user specifies tooth number, tooth width, and tooth contact angle.

1. A trapezoid-shaped tooth on a linear rack slides across the edge of a circular gear with circumference 'C'. A constant rotation rate is desired for the circular gear. The circular gear sweeps out an angle 'A' as the rack tooth travels a distance D, by the relation: A = D * 360 / C. A 'V' shape is created if the rack tooth is allowed to 'carve' into the circular gear. The pattern is symmetrically duplicated based on the desired tooth number. The teeth are 'blunted' by overplotting a calculated addendum circle. The plot is saved as a modifiable image.

2. The gear's shape is highlighted with an interior flood-fill algorithm and a pixel value filter.

3. The gear's edge is traced with a Canny edge detection algorithm.

4. Pixel coordinates are converted back to physical coordinates, to allow the edge points to be arbitrarily scaled and shifted in any coordinate frame.
