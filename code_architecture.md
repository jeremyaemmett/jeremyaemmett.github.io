  # Code architecture

#### _[&larr; VU-MALM](vu_malm.md)_

---

## main.py

### Start-up tasks

- Import packages and subroutines

- Get site data - data.py

- Get forcing data - **[forcing.py](forcing.md)**

- Initialize variables - init.py

- Prepare output files - output2.py

  ### Main computational time loop

  - Get forcing profiles for the day-of-year - **[forcing.py](forcing.md)**
    
  - Calculate DOC profiles given temperature, moisture, and carbon forcing profiles
 
  - Update microbe populations,
      Predict chemistry rates - **[microbes.py](microbes.md)**, **[pathways.py](pathways.md)**

  - Predict diffusion and diffusive surface flux rates - **[diffusion.py](diffusion.md)**
 
  - Predict plant transport and plant-mediated surface flux rates - plants.py
 
  - Adapt the timestep (optional) - newstep.py
 
  - Update model chemistry with predicted diffusion & plant rates - newstep.py
 
  - Write output to file - output2.py

  - Print diagnostic output to the terminal

  - Update the simulation time

## autotuner.py
