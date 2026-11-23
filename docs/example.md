---
file_format: mystnb
kernelspec:
  name: python3
  language: python
---

# Generate even numbers

Our goal is to generate five values, starting at zero.

```{code-cell} ipython3
from sequence import even

n = 5
values = even(n)
print(values)
```

The result contains `n` values, with a spacing of two.
