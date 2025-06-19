import numpy as np
from matplotlib import pyplot as plt
T = np.linspace(-np.pi, np.pi, 1024)
fig, (ax0, ax1) = plt.subplots(ncols =2)
ax0.plot(np.sin(2 * T), np.cos(0.5 * T), c = 'k')
ax1.plot(np.cos(3 * T), np.sin(T), c = 'k')
plt.show()