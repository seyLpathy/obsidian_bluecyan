## 3D散点图
```
# Plotting
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b,
c))
ax.scatter(points[:, 0], points[:, 1], points[:, 2], zdir = 'y',
c = 'k')
```

![[Figure_1.png]]

[[3dscatter.py| *source code*]]

## 3d曲线图
```
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(points[:, 0], points[:, 1], points[:, 2], c = 'k')
plt.show()
```

## 3d曲面图
```
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface(X, Y, Z, cmap=cm.gray)
plt.show()
```

![[Pasted image 20240530144615.png]]