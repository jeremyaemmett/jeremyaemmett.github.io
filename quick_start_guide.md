# Quick Start Guide

#### _[&larr; VU-MALM](vu_malm.md)_

---

## Installation

## Input data

VU-MALM requires 

## Running the model

Use adaptive time stepping if a significant portion or the entirety of the vertical domain is subsaturated. High diffusive gas transport rates can occur across subsaturated layers, and coarse timesteps will result in runaway numerical instability (unrealistically high rates preceding NaN output values), or unrealistic ringing between negative and positive rates.

## Automatic model tuning

Checklist:
  - Set autotune_flag = True _in params.py_
  - Set autotune_name = {desired folder name for tuning results}
  - Set autotune_mode = 'run' _or_ 'plot' _in params.py_, depending on the desired function
  - Set the desired sims_per_first_generation, sims_per_generation, and n_generations _in params.py_
