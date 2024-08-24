# Quick Start Guide

#### _[&larr; VU-MALM](vu_malm.md)_

---

## Installation

## Input data

VU-MALM requires 

## Running the model

Use adaptive time stepping if much or all of the vertical domain consists of subsaturated layers. High diffusive gas transport rates may occur across subsaturated layers, and coarse timesteps will result in runaway numerical instability (unrealistically high rates preceding NaN output values), or unrealistic ringing between negative and positive rates. Numerical stability can be improved by increasing the 'diff_n_dt in _params.py_ (the number of diffusion sub-timesteps within the main computation timestep).

## Automatic model tuning

Checklist:
  - Set autotune_flag = True _in params.py_
  - Set autotune_name = {desired folder name for tuning results}
  - Set autotune_mode = 'run' _or_ 'plot' _in params.py_, depending on the desired function
  - Set the desired sims_per_first_generation, sims_per_generation, and n_generations _in params.py_
