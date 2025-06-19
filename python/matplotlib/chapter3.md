## title
plt.title('A polynomial')
### latex style
plt.title('$f(x)=\\frac{1}{4}(x+4)(x+1)(x-2)$')
## label of axis
```
plt.xlabel('Air speed')
plt.ylabel('Total drag')
## add text
```
plt.text(-0.5, -0.25, 'Brackmard minimum')
### bounding box control
```
box = {
'facecolor' : '.75',
'edgecolor' : 'k',
'boxstyle' : 'round'
}
plt.text(-0.5, -0.20, 'Brackmard minimum', bbox = box)
```

### adding arrows
```
plt.annotate('Brackmard minimum',
ha = 'center', va = 'bottom',
xytext = (-1.5, 3.),
xy = (0.75, -2.7),
arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })
```

## legend
```
plt.plot(X, Y1, c = 'k', lw = 3., label = 'sin(X)')
plt.plot(X, Y2, c = '.5', lw = 3., ls = '--', label = 'cos(X)',col=)
```
col=[[extension#^83b85e|具体位置定义]]
## grid
```
plt.grid(True, lw = 2, ls = '--', c = '.75')
```

## add line
[[line.py|example code]]
![[Pasted image 20240530150045.png]]

## adding shapes
[[shapes.py|example code]]
![[Pasted image 20240530150133.png]]
## tick
```
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.grid(True, which='both')
```

![[Pasted image 20240530150433.png]]
### ticker label
[[ticklabel.py|example code]]
```
ax.xaxis.set_major_locator(ticker.FixedLocator((pos_list)))
ax.xaxis.set_major_formatter(ticker.FixedFormatter((name_list)))
```

![[Pasted image 20240530150658.png]]