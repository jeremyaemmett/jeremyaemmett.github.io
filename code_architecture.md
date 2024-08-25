  # Code architecture

#### _[&larr; VU-MALM](vu_malm.md)_

---

## main.py

### start-up tasks

- **import packages and subroutines**

- **get site data** | data.py

- **get forcing data** | forcing.py

- **initialize variables** | init.py

- **prepare output files** | output2.py

  ### main computatoinal time loop

  - **get forcing profiles for the day-of-year** | forcing.py
    
  - **calculate DOC profiles given temperature, moisture, and carbon forcing profiles**
 
  - **update microbe populations,
      predict chemistry rates** | microbes.py
