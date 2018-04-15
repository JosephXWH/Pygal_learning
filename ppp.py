#coding=utf-8
#计算骰子6，10和的次数
result = []
for i in range(1,7):
	for k in range(1,11):
		p = i + k
		result.append(p)

number = []
for key in range(2,17):
	number.append(result.count(key))
print(number)

