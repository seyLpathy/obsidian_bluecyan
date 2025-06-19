import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
X = np.linspace(0, 6, 1024)
Y1 = np.sin(X)
Y2 = np.cos(X)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(X, Y1, c = 'k', lw = 3., label = 'sin(X)')
plt.plot(X, Y2, c = '.5', lw = 3., ls = '--', label = 'cos(X)')
plt.grid(True, lw = 2, ls = '--', c = '.45')
#ax=plt.axes()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.legend(loc=9)
plt.show()