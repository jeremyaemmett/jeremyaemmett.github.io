
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

The CryoGrid model is initialized with prescribed:
- soil composition (air, water, organic, and mineral volumetric fractions vs. depth)
- ERA5 air temperature and precipitation history
- surface albedo, root decay depth, surface roughness, values, etc.

Choose desired CryoGrid-output data ('T.txt', 'water.txt', etc.) by specifying the name of the CryoGrid output folder, e.g. by setting params.cryogrid_name = 'palsa_low_Drying0p0015_z00p1_rootDepth0p1' in _params.py_.

## Running VU-MALM

### Run '_main.py_'. 
_main.py_ contains calls to every routine and the main computational time loop.

If much of the vertical domain contains subsaturated layers, rapid diffusion through air will occur. There are various ways to improve numerical stability:
  - Set 'dt' = {value} that is <= 0.1/24.0 days
  - Set 'adaptive_dt_flag = True' in _params.py_, which adaptively reduces the time step to ensure that within any layer, removal rates cannot exceed availability.
  - Increase 'diff_n_dt in _params.py_ (the number of diffusion sub-timesteps within the main computation timestep), to make the finite difference scheme 'ring' less in its convergence towards a solution to the Fick's law diffusion equation.

## Automatic model tuning

Checklist:
  - Set autotune_flag = True _in params.py_
  - Set autotune_name = {desired folder name for tuning results}
  - Set autotune_mode = 'run' _or_ 'plot' _in params.py_, depending on the desired function
  - Set the desired sims_per_first_generation, sims_per_generation, and n_generations _in params.py_
