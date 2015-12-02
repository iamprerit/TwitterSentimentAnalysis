import csv
def readfile(filename):
	f=open(filename)
	csv_f=csv.reader(f,delimiter=',',quotechar='|')
	return csv_f