import numpy as np
from matplotlib import pyplot as plt
X = np.linspace(-6, 6, 1024)
Y = np.sinc(X)
X_detail = np.linspace(-3, 3, 1024)
Y_detail = np.sinc(X_detail)
plt.plot(X, Y, c = 'k')
sub_axes = plt.axes([.6, .6, .25, .25])
sub_axes.plot(X_detail, Y_detail, c = 'k')
plt.setp(sub_axes)
plt.show()