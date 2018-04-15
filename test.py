import csv

filename = 'RLC.csv'
with open(filename) as f:
	p = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
	for row in p:
		print(row)