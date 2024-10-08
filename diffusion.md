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

```math
\sigma_{l} = \frac{D_{z} \times dt}{2 \times dz^{2}}
```
      
- Set up a linear system in following matrix form, where $U_{z, \ t+1}$ is the concentration in layer $z$ at the next time step:

$$\begin{bmatrix}1+\sigma & -\sigma & 0 & 0 & 0\\\ -\sigma & 1+2\sigma & -\sigma & 0 & 0\\\ 0 & -\sigma & 1+2\sigma & -\sigma & 0\\\ 0 & 0 & -\sigma & 1+2\sigma & -\sigma\\\ 0 & 0 & 0 & -\sigma & 1+\sigma\end{bmatrix} = \begin{bmatrix}1-\sigma & \sigma & 0 & 0 & 0\\\ \sigma & 1-2\sigma & \sigma & 0 & 0\\\ i & \sigma & 1-2\sigma & \sigma & 0\\\ 0 & 0 & \sigma & 1-2\sigma & \sigma\\\ 0 & 0 & 0 & \sigma & 1-\sigma\end{bmatrix} \begin{bmatrix}U_{1, \ t+1} \\\ U_{2, \ t+1}\\\ U_{3, \ t+1}\\\ U_{4, \ t+1}\\\ U_{5, \ t+1}\end{bmatrix}$$ 

- Modify the concentration in the surface layer as:
```math
U_{1, t+1} = U_{1, t} + F_{srf} \times dt
```
   
- Iteratively solve the linear system for $U_{z, \ t+1}$, the concentration profile at $t+1$.
   
- Correct the concentration profile for conservation loss

- Predict diffusion rates based on the difference between U and U*
   

