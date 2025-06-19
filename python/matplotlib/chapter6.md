##  二维数列可视化
[[squares.py|squares sample]]
![[squares.png]]

==plt.imshow(Z, cmap = cm.binary, extent=(xmin, xmax, ymin, ymax))

### 添加彩色图例
```
cb = plt.colorbar(orientation='horizontal', shrink=.75)
cb.set_label('iteration count')
```