### Algoritms
#### _[&larr; Python Toolbox](python_toolbox.md)_

---

#### Crank-Nicolson Diffussion

```python
def molecular_weight(sub):
    # Output: 'mw_g_mol' = molecular weight of a substance (g/mol)
    # Input: 'sub' lower-case substance name e.g. 'co2'
    mw_g_mol = None
    if sub == 'co2':
        mw_g_mol = 44.01
    if sub == 'c':
        mw_g_mol = 12.0107
    if sub == 'o2':
        mw_g_mol = 31.9988
    if sub == 'ch4':
        mw_g_mol = 16.043
    if sub == 'h2':
        mw_g_mol = 2.016
    if sub == 'ace':
        mw_g_mol = 59.044
    return mw_g_mol
```
