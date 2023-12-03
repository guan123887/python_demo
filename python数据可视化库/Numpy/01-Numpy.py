import numpy as np
x = np.arange(9).reshape((3, 3))
print(x)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""

print(np.diag(x))  # [0 4 8]
print(np.diag(x, k=1))  # [1 5]
print(np.diag(x, k=-1))  # [3 7]

v = [1, 3, 5, 7]
x = np.diag(v)
print(x)