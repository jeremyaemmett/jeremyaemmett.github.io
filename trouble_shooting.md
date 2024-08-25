If the vertical domain contains subsaturated layers, rapid diffusion through air will occur. 
There are various ways to improve numerical stability:
  - Set 'dt' = {value} <= 0.1/24.0 days
  - Set 'adaptive_dt_flag = True' in _params.py_.
      
  This adaptively reduces the time step to ensure that within any layer, removal rates cannot exceed availability.
  - Increase 'diff_n_dt in _params.py_ (the number of diffusion sub-timesteps in timestep dt).

  This makes the finite difference scheme 'ring' less between under/overestimated values, in its convergence towards a solution to the Fick's law diffusion equation.
