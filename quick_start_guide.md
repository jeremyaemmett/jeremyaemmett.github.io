
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

**VU-MALM is by-default configured to receive these from the output of the CryoGrid model.** 

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

If the vertical domain contains subsaturated layers, rapid diffusion through air will occur. 
There are various ways to improve numerical stability:
  - Set 'dt' = {value} <= 0.1/24.0 days
  - Set 'adaptive_dt_flag = True' in _params.py_.
      
  This adaptively reduces the time step to ensure that within any layer, removal rates cannot exceed availability.
  - Increase 'diff_n_dt in _params.py_ (the number of diffusion sub-timesteps in timestep dt).

  This makes the finite difference scheme 'ring' less between under/overestimated values, in its convergence towards a solution to the Fick's law diffusion equation.

## 4. Running VU-MALM

**Run '_main.py_'.** 
_main.py_ calls every routine and contains the main computational time loop.

## 5. Output files

## Automatic model tuning

Checklist:
**1.**
  - Set autotune_flag = True _in params.py_
  - Set autotune_name = {desired folder name for tuning results}
  - Set autotune_mode = 'run' _or_ 'plot' _in params.py_, depending on the desired function
  - Set the desired sims_per_first_generation, sims_per_generation, and n_generations _in params.py_

**2.**
- Run autotune.py
  
  Output is written to: autotune/{site}/{autotune_name}
