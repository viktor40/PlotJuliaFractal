"""
Simple script to plot fractals.
Various comments are placed in places where you can change variables to change the look of the fractal.
"""

import numpy as np
import matplotlib.pyplot as plt


# Set the size of the image (fractal doesn't scale with the sizes, so changing the size might mean some parts of the
# fractal get cut off
m = 480
n = 480

s = 300  # Scale.
x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))
Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

# this is the constant used in the complex polynomials
c = 0.1 + 0.651j

# C is the matrix representing the (complex) constant part of the polynomials
C = np.full((n, m), c)

M = np.full((n, m), True, dtype=bool)
N = np.zeros((n, m))

for i in range(64):  # number of iterations will change the level of detail
    Z[M] = Z[M] * Z[M] + C[M]  # set of complex polynomials as matrices
    M[np.abs(Z) > 2] = False
    N[M] = i


fig = plt.figure()
fig.set_size_inches(m / 100, n / 100)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
ax.set_xticks([])
ax.set_yticks([])

# you can change the color map (cmap) to different maps for different colours in hte plot
# more color maps can be found at https://matplotlib.org/3.3.2/tutorials/colors/colormaps.html
plt.imshow(np.flipud(N), cmap='inferno')
plt.savefig('julia.png')
plt.show()
