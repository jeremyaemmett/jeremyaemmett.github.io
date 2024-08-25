  # Code architecture

#### _[&larr; VU-MALM](vu_malm.md)_

---

## main.py

### start-up tasks

- import packages and subroutines

- **get site data** | data.py

- **get forcing data** | forcing.py

- **initialize variables** | init.py

- **prepare output files** | output2.py

  ### main computatoinal time loop

  - **get forcing profiles for the day-of-year** | forcing.py
    
  - calculate DOC profiles given temperature, moisture, and carbon forcing profiles
 
  - **update microbe populations,
      predict chemistry rates** | microbes.py, pathways.py

  - **predict diffusion and diffusive surface flux rates** | diffusion.py
 
  - **predict plant transport and plant-mediated surface flux rates** | plants.py
 
  - **Adapt the timestep (optional)** | newstep.py
 
  - **Update model chemistry with predicted diffusion & plant rates** | newstep.py
 
  - **Write output to file** | output2.py

  - Print diagnostic output to the terminal

  - Update the simulation time
