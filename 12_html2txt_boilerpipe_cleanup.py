"""
========================================================
html2txt
========================================================

Change: apply the html2text library to improve paragraphing quality
Install html2text in the folder /html2text.zip

Refined version of html2txt:
1) Parsing html using lxml
2) Well-handled domain name extraction
3) In-depth cleanup that cleans all meaningless tabs, spaces, empytlines
4) Clean-up lines that are shorter than a given length (line 82)
5) Cutomized input (.txt file that contains url to the target .html files, one url each line)
"""

import os
import re
import glob
import StringIO

print __doc__

#################################################
# Function for cleanup the text:
# 1: clearnup: 1)tabs, 2)spaces, 3)empty lines;
# 2: remove short lines
# 
# v3 adding &nbsp_place_holder; cleanup
# 
def textcleanup(text, line_threshold=0):
    # temp list for processing
    text_list = []
    for s in text.splitlines():
        # v3: handle &nbsp_place_holder; into space
        s = s.replace('&nbsp_place_holder;', ' ')
        # Strip out meaningless spaces and tabs
        s = s.strip()
        # New improvement: removing all extra spaces
        s = re.sub(r' +', ' ', s)
        # Set length limit
        if s.__len__() > line_threshold:
            text_list.append(s)
    cleaned = os.linesep.join(text_list)
    # Get rid of empty lines
    cleaned = os.linesep.join([s for s in cleaned.splitlines() if s])
    return cleaned


# read every file in folder, do the cleanup, 
# then write back to a file in the new folder
for file_item in glob.glob("txtou_bpArticle/*.txt"):
    # get the file number for current opened file
    # [16:-4] means from the 17th letter from top to 4th letter from back
    # this specifically matches the patter of 'txtou_bpArticle/NUMBER.txt'
    file_num = file_item[16:-4]
    g = open(file_item)
    # object.read() is the right way to 
    content = g.read()
    # cleanup
    cleaned = textcleanup(content, line_threshold=50)
    # write back
    f = open('txtou_bpArticleC/'+file_num+'.txt', 'wb')
    f.write(cleaned)
    f.close()
    g.close()

print 'Done!'
