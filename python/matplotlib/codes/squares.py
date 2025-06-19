import numpy as np
import matplotlib.cm as cm
from matplotlib import pyplot as plt
def iter_count(C, max_iter):
    X = C
    for n in range(max_iter):
        if abs(X) > 2.:
            return n
        X = X ** 2 + C
    return max_iter
N = 512
max_iter = 64
xmin, xmax, ymin, ymax = -2.2, .8, -1.5, 1.5
X = np.linspace(xmin, xmax, N)
Y = np.linspace(ymin, ymax, N)
Z = np.empty((N, N))
for i, y in enumerate(Y):
    for j, x in enumerate(X):
        Z[i, j] = iter_count(complex(x, y), max_iter)
plt.imshow(Z, cmap = cm.binary,extent=(xmin,xmax,ymin,ymax))
plt.show()