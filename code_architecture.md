  # Code architecture

#### _[&larr; VU-MALM](vu_malm.md)_

---

## main.py

### Start-up tasks

- Import packages and subroutines

- **Get site data** | data.py

- **Get forcing data** | forcing.py

- **Initialize variables** | init.py

- **Prepare output files** | output2.py

  ### Main computational time loop

  - **Get forcing profiles for the day-of-year** | forcing.py
    
  - Calculate DOC profiles given temperature, moisture, and carbon forcing profiles
 
  - **Update microbe populations,
      Predict chemistry rates** | microbes.py, pathways.py

  - **Predict diffusion and diffusive surface flux rates** | diffusion.py
 
  - **Predict plant transport and plant-mediated surface flux rates** | plants.py
 
  - **Adapt the timestep (optional)** | newstep.py
 
  - **Update model chemistry with predicted diffusion & plant rates** | newstep.py
 
  - **Write output to file** | output2.py

  - Print diagnostic output to the terminal

  - Update the simulation time

## autotuner.py
