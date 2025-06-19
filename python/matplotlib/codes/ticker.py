import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
def make_label(value, pos):
	return '%0.1f%%' % (100. * value)
ax = plt.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))
X = np.linspace(0, 1, 256)
plt.plot(X, np.exp(-10 * X), c ='k')
plt.plot(X, np.exp(-5 * X), c= 'k', ls = '--')
plt.show()