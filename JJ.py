#coding=utf-8
import pygal

line_chart = pygal.HorizontalStackedBar()
line_chart.title = '珏珏运动数据记录(distance--km)'
line_chart.x_labels = ['2017.2.3','2017.3.4','2017.3.9','2017.4.5']
line_chart.add('跑步',[2.31,5.56,7.8,4.5])
line_chart.add('散步',[10.8,6.9,7.2,8.5])
line_chart.render_to_file('JJ.svg')
