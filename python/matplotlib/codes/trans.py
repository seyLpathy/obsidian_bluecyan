import numpy as np
import matplotlib.pyplot as plt
name_list = ('Omar', 'Serguey', 'Max', 'Zhou', 'Abidin')
value_list = np.random.randint(99, size=len(name_list))
pos_list = np.arange(len(name_list))
plt.bar(pos_list, value_list, alpha = .75, color = '.75', align =
'center')
plt.xticks(pos_list, name_list)
plt.savefig('bar.png', transparent = True)