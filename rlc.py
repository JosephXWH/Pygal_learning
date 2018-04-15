#coding=utf-8
import csv
import pygal

filename = 'RLC.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	Hz = []
	Uro100 = []
	I100 = []
	Uro300 = []
	I300 = []
	
	for row in reader:
		Hz.append(int(row[0]))
		I100.append(float(row[2]))
		I300.append(float (row[4]))

line_chart = pygal.Line(fill = True, interpolate = 'cubic',
	x_label_rotation = 45, x_title = '频率(Hz)', y_title = '电流(mA)')
line_chart.x_labels = Hz
line_chart.title = ' RLC谐振模拟实验数据'
line_chart.add('100Ω', I100)
line_chart.add('300Ω', I300)

line_chart.render_to_file('D.svg') 