## Python Toolbox

[a relative link](https://jeremyaemmett.github.io/2021/03/08/test.html)

Handy custom Python bits and pieces

---

### Plotting

#### _Neatly format an axis_

```python
def format_axis1(ax):

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_facecolor('whitesmoke')
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5, axis='y')

    return()
```

### Unit Conversions

### File Handling

#### _Find files by type_

```python
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
```

#### _Read a CSV column_

```python
def read_csv_header(filename, column_idx, var_type, header_lines):
    with open(filename) as f:
        reader = csv.reader(f)
        if header_lines != 0:
            for h in range(0,header_lines):
                header = next(reader)
        vals = []
        for row in reader:
            if var_type == 'string':
                val = row[column_idx]
            if var_type == 'integer':
                val = int(row[column_idx])
            if var_type == 'float':
                if row[column_idx] == '':
                    val = -9999.0
                else:
                    val = float(row[column_idx])
            vals.append(val)
    return vals
```

#### _Read CSV data into a list_

```python
def read_csv_array(filename):

    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return(data)
```



