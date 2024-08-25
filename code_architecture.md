# Code architecture

#### _[&larr; VU-MALM](vu_malm.md)_

---

## main.py

**import packages and subroutines**

**import site data**
  data.py 
    -> measured composition profiles, time series, etc., interpolated to the model depth grid

**import forcing data**
  forcing.py
    -> depth vs. time. vs value arrays of temperature, moisture, and carbon, interpolated to the model depth grid

**initialize variables**
  init.py
    -> 
