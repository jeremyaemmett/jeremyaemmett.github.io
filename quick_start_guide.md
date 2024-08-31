
# Quick Start Guide

#### _[&larr; VU-MALM](vu_malm.md)_

---

## 1. Installation

## 2. Input data

**VU-MALM's minimum input data are vertical soil profiles of daily-mean:** 
- temperature (degC)
- moisture (m3/m3)
- carbon (m3/m3)
...specified for each day of year over a full year.

The CryoGrid model is initialized with prescribed:
- soil composition (air, water, organic, and mineral volumetric fractions vs. depth)
- ERA5 air temperature and precipitation history
- surface albedo, root decay depth, surface roughness, values, etc.

Choose desired CryoGrid-output data ('T.txt', 'water.txt', etc.) by specifying the name of the CryoGrid output folder, e.g. by setting params.cryogrid_name = 'palsa_low_Drying0p0015_z00p1_rootDepth0p1' in _params.py_.

## 3. Set-up parameters

**On/Off switches, constants, and initial values are specified in _params.py_.**

Make sure to specify:
  - **dt** (main computational timestep [days])
  - **nz** (number of vertical layers)
  - **dz** (layer thicknesses)
  - **diff_n_dt** (number of diffusion scheme sub-timesteps)
  - **write_dt** (output write interval [days])
  - **test_datetime** (starting datetime e.g. 'datetime(2022, 8, 1, 0, 0, 0)')
  - **years** (number of simulated years - output will be written in this year [int])

## 4. Running VU-MALM

**Run '_main.py_'.** 
_main.py_ calls all routines and contains the main computational time loop.

## 5. Output

  ### File Output

  ### Console Output

  Prints fluxes every 1st and 15th of each month. Prints detailed profile and yearly budget data every Aug 15th.

## Automatic model tuning

**1.**

Checklist:
  - Set autotune_flag = True _in params.py_
  - Set autotune_name = {desired folder name for tuning results}
  - Set autotune_mode = 'run' _or_ 'plot' _in params.py_, depending on the desired function
  - Set the desired sims_per_first_generation, sims_per_generation, and n_generations _in params.py_

**2.**
- Run autotune.py
  
  Output is written to: autotune/{site}/{autotune_name}
