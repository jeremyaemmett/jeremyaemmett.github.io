### Algorithms
#### _[&larr; Python Toolbox](python_toolbox.md)_

---

#### Crank-Nicolson Diffusion

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
from plotly.subplots import make_subplots
import plotly.io as pio
import transport
import forcing
import params
from copy import copy
import init

def cn_solver(T_record,n_dx,dx,n_tx,dt,diff,x_atmos):

    # Diffusion coefficients
    r = diff * dt /2 /dx**2

    # Banded 'AB' array (rows = diagonal values of the tri-diagonal 'A' array)
    a = np.zeros((3, n_dx - 1))
    a[0, 1:] = -r[0:(n_dx - 2)]  # j-1
    a[1, :] = (1 + 2 * r[0:(n_dx - 1)])  # j
    a[1, (n_dx - 2)] = (1 + r[n_dx - 2])  # j
    a[2, :-1] = -r[1:(n_dx - 1)]  # j+1
    a[2, (n_dx - 2)] = 0  # j+1

    # Initialize the 'B' array
    b = np.zeros(n_dx - 1)

    # Loop within the main computational time step
    T = T_record[0:n_dx]
    T_records=[]
    T[0] = x_atmos
    for i in range(1, n_tx + 1):

        # Calculate the indices of the 'B' array with corresponding r (diff) coefficients
        ri = r[1]
        b[0] = ri * T[0] + (1 - 2 * ri) * T[1] + ri * T[2]
        ri = r[2:-1]
        b[1:-1] = ri * T[1:-2] + (1 - 2 * ri) * T[2:-1] + ri * T[3:]
        ri = r[0]
        b[0] = b[0] + ri * T[0]
        ri = r[(n_dx - 2)]
        b[(n_dx - 2)] = ri * T[(n_dx - 2) - 1] + (1 - ri) * T[(n_dx - 2)]

        # Solve the linear system 'Ax = B' for x (unknown values at the next time step)
        T[1:] = solve_banded((1, 1), a, b)

        # Record the solution to account for freeze/thaw (which vertically moves the lower boundary level)
        T_record[0:n_dx] = T

    return(T_record)
    
```
