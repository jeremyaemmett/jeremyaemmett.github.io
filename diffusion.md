# diffusion.py

Source Code:
[diffusion.py](https://github.com/jeremyaemmett/VU-MALM/blob/main/diffusion.py)

This sentence uses `$` delimiters to show math inline:  
```math
\sqrt{3x-1}+(1+x)^2
```

## def diffusion_cranknicolson2

  - Get the subset of layers that are unfrozen (diffusion only occurs in these). This is 'U'

  - Calculate surface fluxes, so the surface layer concentration can be modified

    ## def cn_diffusion

      - Calculate layer $\sigma$ values from the layer diffusivities, accounting for the diffusion time step:
      
      - Set up a linear system in matrix form: A = B dot U*, where:

        A = test, B = test, and U* = the future concentration profile

$$\begin{bmatrix}1+\sigma & -\sigma & 0 & 0 & 0\\\ -\sigma & 1+2\sigma & -\sigma & 0 & 0\\\ 0 & -\sigma & 1+2\sigma & -\sigma & 0\\\ 0 & 0 & -\sigma & 1+2\sigma & -\sigma\\\ 0 & 0 & 0 & -\sigma & 1+\sigma\end{bmatrix} = \begin{bmatrix}a & \sigma & c & d & d\\\ \sigma & f & \sigma & h & h\\\ i & \sigma & k & \sigma & l\\\ m & n & \sigma & p & \sigma\\\ q & r & s & \sigma & t\end{bmatrix} \begin{bmatrix}a \\\ b\\\ c\\\ d\\\ d\end{bmatrix}$$ 

      - Give the surface layer concentration (U*[0]) its expected value at the next main time step, according to the computed surface flux
   
      - Iteratively solve for the concentration profile at the next main time step
   
      - Correct the concentration profile for conservation loss

    - Predict diffusion rates based on the difference between U and U*
   

