import csv
def readfile(filename):
	f=open(filename)
	csv_f=csv.reader(f,delimiter=',',quotechar='"')
	# for x in csv_f:
	# 	print (x)
	return csv_f

#readfile("traindata1.csv")