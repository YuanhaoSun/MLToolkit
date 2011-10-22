"""
Use a .csv file as input, output txt files.
Treat first column as label and save second column into a txt file.
Txt files are stored in different folders by labels.
"""
print __doc__

import csv, os
with open('lpp.csv', 'r') as csvf:
    reader = csv.reader(csvf)
    rownumber = 0
    for row in reader:
    	label = row[0]
    	
    	# try to create new folder for new label
    	# os.path.dirname(__file__) or os.getcwd() is the dir of current .py file
    	dir = os.path.dirname("%s/%s/" % ( os.getcwd(), label ) )
    	if not os.path.exists(dir):
   			os.makedirs(dir)
		
        g = open(os.getcwd() + "/" + label + "/" + str(rownumber+1) + ".txt","w")
        g.write(row[1])
        rownumber = rownumber + 1
        g.close()