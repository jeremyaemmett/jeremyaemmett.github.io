## Python Toolbox

Handy custom Python bits and pieces

---

### [Plotting](/plotting.html)

#### _Neatly format an axis_

```python
def format_axis1(ax):

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_facecolor('whitesmoke')
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5, axis='y')

    return()
```
