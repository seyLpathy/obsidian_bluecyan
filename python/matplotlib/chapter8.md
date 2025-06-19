## user control plot
key-functions:
```
ax = fig.add_subplot(111, polar = True)
ax_m = plt.axes([0.05, 0.05, 0.25, 0.025])
添加新的数轴
slider_m = Slider(ax_m, 'm', 1, 20, valinit = m_init)
绑定滑块
lines.set_ydata(r)
重新绘制图
fig.canvas.draw_idle()
#refresh
slider_n1.on_changed(update)
#滑块滑动时回调对应函数
```