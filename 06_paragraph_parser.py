import os
import lxml.html


htmltree = lxml.html.parse('http://www.bigfishgames.com/company/privacy.html')

# Parse out all the <p> paragraphs
p_tags = htmltree.xpath('//p')
p_content = [p.text_content() for p in p_tags]

# Parse out all the <li> paragraphs
li_tags = htmltree.xpath('//li')
li_content = [li.text_content() for li in li_tags]

# counter for filenames
filenumber = 0

for item in p_content:
	# Remove all paragraphs shorter than 50 bytes
	if item.__len__() > 50:
		print [item.__len__(), filenumber+1]
		g = open( os.getcwd() + "/paragraphs/" + str(filenumber+1) + ".txt","w")
		g.write( item.encode('ascii', 'ignore') )
		filenumber = filenumber + 1
		g.close()

for item in li_content:
	# Remove all list items shorter than 50 bytes
	if item.__len__() > 50:
		print [item.__len__(), filenumber+1]
		g = open( os.getcwd() + "/paragraphs/" + str(filenumber+1) + ".txt","w")
		g.write( item.encode('ascii', 'ignore') )
		filenumber = filenumber + 1
		g.close()

print 'Done'