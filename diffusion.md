# diffusion.py

This sentence uses `$` delimiters to show math inline:  $\sqrt{3x-1}+(1+x)^2$

## def diffusion_cranknicolson2

  - Get the subset of layers that are unfrozen (diffusion only occurs in these). This is 'U'

  - Calculate surface fluxes, so the surface layer concentration can be modified

    ## def cn_diffusion

      - Calculate layer 'sigma' values from the layer diffusivities, accounting for the diffusion time step:
      
      - Set up a linear system in matrix form: A = B dot U*, where:

        A = test, B = test, and U* = the future concentration profile

        \begin{equation}
\begin{pmatrix}
  1       & x^1_0   & x^2_0   & \cdots  & x^{degree}_0  \\
  1       & x^1_1   & x^2_1   & \cdots  & x^{degree}_1  \\
  \vdots  & \vdots  & \vdots  & \ddots  & \vdots \\
  1       & x^1_n   & x^2_n   & \cdots  & x^{degree}_n  \\
\end{pmatrix}
\end{equation}

```math
\begin{bmatrix}X\\Y\end{bmatrix}
```

      - Give the surface layer concentration (U*[0]) its expected value at the next main time step, according to the computed surface flux
   
      - Iteratively solve for the concentration profile at the next main time step
   
      - Correct the concentration profile for conservation loss

    - Predict diffusion rates based on the difference between U and U*
   

