# diffusion.py

This sentence uses `$` delimiters to show math inline:  $\sqrt{3x-1}+(1+x)^2$

## def diffusion_cranknicolson2

  - Get the subset of layers that are unfrozen (diffusion only occurs in these)

  - Calculate surface fluxes, so the surface layer concentration can be modified

    ## def cn_diffusion

      - Calculate layer 'sigma' values from the layer diffusivities:
      
      - Set up a linear system in matrix form: A = B dot U, where:

        A = test, B = test, and U = the concentration profile at the next diffusion time step
