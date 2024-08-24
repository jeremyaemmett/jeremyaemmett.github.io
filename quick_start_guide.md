# Quick Start Guide

#### _[&larr; VU-MALM](vu_malm.md)_

---

## Installation

## Input data

VU-MALM's minimum input data are vertical profiles of daily-mean soil temperature, moisture, and carbon profiles, specified for each day of year over a full year.

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
