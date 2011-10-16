"""
Use a .csv file as input, output txt files.
Treat first column as label and save second column into a txt file.
All txt files are stored in the same folder
"""
print __doc__

import csv
with open('lpp.csv', 'r') as f:
    reader = csv.reader(f)
    rownumber = 0
    for row in reader:
    	label = row[0]
        g = open(label + str(rownumber+1) + ".txt","w")
        g.write(row[1])
        rownumber = rownumber + 1
        g.close()