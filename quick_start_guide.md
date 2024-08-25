
# Quick Start Guide

#### _[&larr; VU-MALM](vu_malm.md)_

---

## Installation

## Input data

### VU-MALM's minimum input data are vertical soil profiles of daily-mean: 
- temperature (degC)
- moisture (m3/m3)
- carbon (m3/m3)
...specified for each day of year over a full year.

### VU-MALM is configured by default to receive these from the output of the CryoGrid model. 

The CryoGrid model is initialized with a prescribed:
- soil composition profile (air, water, organic, and mineral volumetric percentages vs. depth)
- ERA5 air temperature and precipitation history vs. time
- surface albedo, root decay depth, surface roughness, etc.

Choose desired CryoGrid-output data ('T.txt', 'water.txt', etc.), by specifying the name of the CryoGrid folder containing those files: i.e./e.g. by specifying params.cryogrid_name = 'palsa_low_Drying0p0015_z00p1_rootDepth0p1' in _params.py_.

## Running the model

If much of the vertical domain consists of subsaturated layers, either:
  - Set 'adaptive_dt_flag = True' in _params.py_
  - Set 'dt' = {value <= 0.1/24.0 days}
To avoid numerical instability (unrealistically high rate magnitudes, NaNs, and positive/negative ringing)
Numerical stability can be further improved by increasing the 'diff_n_dt in _params.py_ (the number of diffusion sub-timesteps within the main computation timestep).

## Automatic model tuning

Checklist:
  - Set autotune_flag = True _in params.py_
  - Set autotune_name = {desired folder name for tuning results}
  - Set autotune_mode = 'run' _or_ 'plot' _in params.py_, depending on the desired function
  - Set the desired sims_per_first_generation, sims_per_generation, and n_generations _in params.py_
