## 多图绘制
[[subplot.py|sample code1]]
[[subplot2.py|sample code2]]

``` 
import numpy as np
from matplotlib import pyplot as plt
T = np.linspace(-np.pi, np.pi, 1024)
grid_size = (4, 2)
plt.subplot2grid(grid_size, (0, 0), rowspan = 3, colspan = 1)
plt.plot(np.sin(2 * T), np.cos(0.5 * T), c = 'k')
plt.subplot2grid(grid_size, (0, 1), rowspan = 3, colspan = 1)
plt.plot(np.cos(3 * T), np.sin(T), c = 'k')
plt.subplot2grid(grid_size, (3, 0), rowspan=1, colspan=3)
plt.plot(np.cos(5 * T), np.sin(7 * T), c= 'k')
plt.tight_layout()
plt.show()
```

### function
1. subplot2grid
	tuple(网格的行数和列数)
	网格中的坐标
	rowspan
	colspan

2. subplot() 
	1. 参数 行与列
	2. 返回值 figure object 和 对应规模的Axes

## 数轴
### x/y ratio 
```
plt.axes().set_aspect('equal')
```

### 数轴长度
>[!code]
>pyplot.xlim()
>pyplot.ylim()

### figure size
[[ratio.py|sample code]]
![[Pasted image 20240530002609.png]]
## 图的内嵌
[[embbed.py.py|图的内嵌]]
sub_axes = plt.axes([left,bottom,width,height])
plt.setp(sub_axes)
## 数轴转化
### 对数
```
plt.xscale('symlog', linthreshx=6.)
```

### 极坐标
```
plt.axes(polar = True)
```
![[Pasted image 20240530004151.png]]

