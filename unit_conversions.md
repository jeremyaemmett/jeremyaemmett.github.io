### Unit Conversions
#### _[&larr; Python Toolbox](python_toolbox.md)_

---

#### Molecular weight of a molecule

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

def mol2kg(mol, sub):
    # Output: 'kg' kilograms of a substance (kg)
    # Input: 'mol' moles of a substance (mol); 'sub' lower-case substance name e.g. 'co2'
    mw_g_mol = molecular_weight(sub)
    mw_kg_mol = mw_g_mol / 1000.0
    kg = mol * mw_kg_mol
    return kg

```python
def mol2g(mol, sub):
    # Output: 'g' kilograms of a substance (kg)
    # Input: 'mol' moles of a substance (mol); 'sub' lower-case substance name e.g. 'co2'
    mw_g_mol = molecular_weight(sub)
    g = mol * mw_g_mol
    return g
```

```python
def ug2umol(ug, sub):
    # Output: 'umol' micromoles of a substance (umol)
    # Input: 'ug' micrograms of a substance (ug); 'sub' lower-case substance name e.g. 'co2'
    mw_g_mol = molecular_weight(sub)
    mw_mol_ug = 1.0 / ((1e6) * mw_g_mol)
    mol = ug * mw_mol_ug
    umol = (1e6) * mol
    return umol
```

```python
def umol2g(umol, sub):
    # Output: 'g' grams of a substance (kg)
    # Input: 'umol' micromoles of a substance (umol); 'sub' lower-case substance name e.g. 'co2'
    mw_g_mol = molecular_weight(sub)
    mw_g_umol = mw_g_mol/(1e6)
    g = umol * mw_g_umol
    return g
```

```python
def kg2mol(kg, sub):
    # Output: 'mol' moles of a substance (mol)
    # Input: 'kg' kilograms of a substance (kg); 'sub' lower-case substance name e.g. 'co2'
    mw_g_mol = molecular_weight(sub)
    mw_mol_kg = 1000.0 / mw_g_mol
    mol = kg * mw_mol_kg
    return mol
```

```python
def ppm2molm3(ppm, sub):
    # Output: 'molm3' moles of a gas per cubic meter of air at 1 atm and 25 degC (m3)
    # Input: 'ppm' parts per million of a gas in air at 1 atm and 25 degC (ppm); 'sub' lower-case substance name e.g. 'co2'
    mgm3 = 0.0409 * ppm * molecular_weight(sub)
    gm3 = 0.001 * mgm3
    molm3 = gm3 / molecular_weight(sub)
    return molm3
```
