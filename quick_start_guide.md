
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

These input data can, for example, be extrapolated separately by land-surface models, e.g. CryoGrid.
CryoGrid is initialized with prescribed:
- soil composition (air, water, organic, and mineral volumetric fractions vs. depth)
- ERA5 air temperature and precipitation history
- surface albedo, root decay depth, surface roughness, values, etc.

Choose desired CryoGrid-output data ('T.txt', 'water.txt', etc.) by specifying the name of the forcing data folder, e.g. by setting forcing_file = 'palsa_low_Drying0p0015_z00p1_rootDepth0p1' in _parameters.py_.

## 3. Set-up parameters

**On/Off switches, constants, and initial values are specified in _params.py_.**

Make sure to specify:
  - **dt** (main computational timestep [days])
  - **dz0** (initial layer thickness)
  - **growth_rate** (factor by which layer thickness grows exponentially)
  - **total_depth** (total depth of the layer column (m))
  - **diff_n_dt** (number of diffusion scheme sub-timesteps)
  - **diff_n_dz** (number of diffusion layers (uniform thickness) to total_depth)
  - **write_dt** (output write interval [days])
  - **start_datetime** (starting datetime e.g. 'datetime(2022, 8, 1, 0, 0, 0)')
  - **end_datetime** (ending datetime e.g. 'datetime(2022, 8, 1, 0, 0, 0)')
  - **instant_diffusion*** (set 'True' to assume instant layer-atmosphere diffusion for layers above the water table)
  - **interface_flux** (set 'True' to diffusively couple concentrations in the water table layer to concentratios in the overlying sub-saturated column)
  - **gaussian_profile*** (set 'True' to initiate the model with gaussian concentration profiles, for testing)

Chemical species, chemical species attributes, reaction pathways, reaction parameters, and associated microbe groups are specified by the user in standard-formatted dictionary blocks.

## 4. Running VU-MALM

**Run '_main.py_'.** 
_main.py_ calls all routines and contains the main computational time loop.

## 5. Output

  _output.py_ writes time-stamped output to ASCII files every write_timestep.
