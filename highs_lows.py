#coding=utf-8
import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取日期和最高温度
filename = '2017.csv'
with open(filename) as f:
	print(csv.reader(f))
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates,highs,lows = [],[],[]
	for row in reader:
		current_date = datetime.strptime(row[0],"%Y/%m/%d")
		dates.append(current_date)
		highs.append(int(row[1]))
		lows.append(int(row[3]))

fig = plt.figure(dpi=128, figsize = (10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows,facecolor = 'blue', alpha=0.1)
#设置图形的属性
plt.title("Daily high and low temperatures, Whole 2017", fontsize=24)
plt.xlabel ('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel ("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize = 16)

plt.show()