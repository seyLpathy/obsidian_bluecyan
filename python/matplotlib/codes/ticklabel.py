import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
name_list = ('Omar', 'Serguey', 'Max', 'Zhou', 'Abidin')
value_list = np.random.randint(0, 99, size = len(name_list))
pos_list = np.arange(len(name_list))
ax = plt.axes()
##
ax.xaxis.set_major_locator(ticker.FixedLocator((pos_list)))
ax.xaxis.set_major_formatter(ticker.FixedFormatter((name_list)))
##
plt.bar(pos_list, value_list, color = '.75', align = 'center')
plt.show()