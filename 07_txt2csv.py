import os, glob, csv

csvWriter = csv.writer(open("csvfile.csv","wb"))

for files in glob.glob("*.txt"):
	g = open(files)
	rows = g.readlines()
	# write to first column
	csvWriter.writerow(rows)
	# write to second column
	# csvWriter.writerow([' '] + [rows])