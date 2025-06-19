import matplotlib.pyplot as plt
N = 16
for i in range(N):
	plt.gca().add_line(plt.Line2D((0, i), (N - i, 0), color = '.75'))
# gca() to render and call function add_line()
plt.grid(True)
plt.axis('scaled')
plt.show()