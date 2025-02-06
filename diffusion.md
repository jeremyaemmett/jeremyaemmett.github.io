# diffusion.py

Source Code:
[diffusion.py](https://github.com/jeremyaemmett/VU-MALM/blob/main/diffusion.py)

![vumalm_transport1](https://github.com/user-attachments/assets/17bafe12-188a-48fe-93dc-58c1833157f5)

Vertical gas diffusion below-ground results from variations in gas concentration between model layers. The flow rate within a given layer is modulated by its material diffusivity, such that higher diffusivity results in higher flow rates. Diffusivity is inversely proportational to soil pore saturation, reflecting faster rates of gas diffusion through airy as opposed to water-logged material.

 Diffusion rates are solved using an implicit Crank-Nicolson (CN) finite difference scheme that treats the permafrost interface as an insulated boundary (through which gas cannot flow, represented there by a zero-derivative gas concentration gradient), and the uppermost soil layer as an open boundary that is coupled to the atmosphere via a water-to-air interface flux calculation.

## def diffusion_cranknicolson2

  - Get the subset of layers 'U' that are unfrozen (where diffusion can occur).

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

## def partial_pressure

  - Calculate the partial pressure of each gas in air, assuming a total air partial pressure (pa_air) of 101.325e3 Pa, and respective CH4, O2, CO2, and H2 volume fractions (vol_x) of 0.000179, 20.946, 0.0412, 0.00005.

pa_x = (vol_x / 100.0) * pa_air

## def equilibrium_concentration

 - Calculate the equilibrium concentration of each gas (which would produce a pressure counterbalancing the gas' partial pressure).

    - Calculate Henry's constant (H_x) for each gas, following Sander (2015), using respective CH4, O2, CO2, and H2 leading factors (K_x) of 1.3e-3, 1.3e-3, 3.4e-2 and 7.8e-4, and exponential factors (C_x) of 1700.0, 1500.0, 2400.0 and 530.0.
  
      H_x = K_x * exp(C_x * (1 / (T + 273.15) - (1 / 273.15)))
  
      

## def schmidt_number

## def transfer_velocity

## def surface_flux

## def diffusivity

## def effective_diffusivity
   

