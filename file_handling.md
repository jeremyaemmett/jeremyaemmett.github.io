### File Handling
#### _[&larr; Python Toolbox](python_toolbox.md)_

---

#### Find all files in a directory, containing a given substring

```python
import os

def files_with_substring(folder, substring):

    # Find all files in the specified folder
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and substring in f]

    return files
```

#### Find files by type

```python
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
```

#### Read a CSV column

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

#### Read CSV data into a list

```python
def read_csv_array(filename):

    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return(data)
```
