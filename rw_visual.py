#coding=utf-8
import matplotlib.pyplot as plt 

from random_walkk import RandomWalk 
#创建一个 RandomWalk 实例，并将其中的点都绘制出来
rw = RandomWalk()
rw.fill_walk()

#设置绘图窗口的尺寸
plt.figure(figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_value, rw.y_value, c=point_numbers,
 cmap=plt.cm.Blues, edgecolor='none', s=15)

#突出起点和重点
plt.scatter(0,0, c='green', edgecolor='none',s=100)
plt.scatter(rw.x_value[-1],rw.y_value[-1],edgecolor='none',
	s=100)

#隐藏坐标
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()