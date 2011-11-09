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

from __future__ import with_statement
from urlparse import urlparse
from urllib2 import urlopen

import html2text
from django.utils import encoding

import os
import re
import StringIO
import lxml.html


print __doc__


#################################################################################
# Auxiliary function for converting unicode to string, 
# using django.utils.encoding
def convert_unicode_to_string(x):
    """
    >>> convert_unicode_to_string(u'ni\xf1era')
    'niera'
    """
    return encoding.smart_str(x, encoding='ascii', errors='ignore')


#################################################################################
# Auxiliary function and file for correctly extract domain from url
# Author:
# http://stackoverflow.com/questions/1066933/python-extract-domain-name-from-url
# load tlds, ignore comments and empty lines:
with open("effective_tld_names.dat.txt") as tldFile:
    tlds = [line.strip() for line in tldFile if line[0] not in "/\n"]

def getDomain(url, tlds):
    urlElements = urlparse(url)[1].split('.')
    # urlElements = ["abcde","co","uk"]

    for i in range(-len(urlElements),0):
        lastIElements = urlElements[i:]
        #    i=-3: ["abcde","co","uk"]
        #    i=-2: ["co","uk"]
        #    i=-1: ["uk"] etc

        candidate = ".".join(lastIElements) # abcde.co.uk, co.uk, uk
        wildcardCandidate = ".".join(["*"]+lastIElements[1:]) # *.co.uk, *.uk, *
        exceptionCandidate = "!"+candidate

        # match tlds: 
        if (exceptionCandidate in tlds):
            return ".".join(urlElements[i:]) 
        if (candidate in tlds or wildcardCandidate in tlds):
            return ".".join(urlElements[i-1:])
            # returns "abcde.co.uk"

    raise ValueError("Domain not in global list of TLDs")
# print getDomain("http://abcde.co.uk",tlds)


# Function for html2txt using lxml
# Author:
# http://groups.google.com/group/cn.bbs.comp.lang.python/browse_thread/thread/781a357e2ce66ce8
def html2txt(html):
    tree = lxml.etree.fromstring(html, lxml.etree.HTMLParser()) if isinstance(html, basestring) else html 
    for skiptag in ('//script', '//iframe', '//style', 
                    '//link', '//meta', '//noscript', '//option'):    
        for node in tree.xpath(skiptag):
            node.getparent().remove(node)
    # return lxml.etree.tounicode(tree, method='text')
    return lxml.etree.tostring(tree, encoding=unicode, method='text')


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


# Read from a hard-coded file with each url as a line
ppfile = open('urls.txt', 'r')


# counter is the index counter for number of iterations
for counter, line in enumerate(ppfile):

    # domain could be out scope of global list of TLDs
    try:
        # get the domain from url for naming of the txt file
        domain = getDomain(line, tlds)
    except:
        domain = str(line[0:15])
        pass

    # urls in each line -- called line here.
    line = line.rstrip('\n')


    ###################################
    # html2text using html2text
    # Initialiate an instance of HTML2Text for extracting text
    h = html2text.HTML2Text()
    h.ignore_links = True   # ignore content of urls in html
    h.ignore_images = True
    h.body_width = 0        # not wrap the lines

    # read from url
    try:
        link_open = urlopen(line)
        data = link_open.read()
    except:
        print 'cannot open: ', line
        pass
        data = line
    # formatting raw data
    data = unicode(data, "utf8", "ignore")
    data = convert_unicode_to_string(data)
    
    # using HTML2Text to handle text
    try:
        text = h.handle(data)
        output = convert_unicode_to_string(text)
        print 'h2t : ', line

        # cleanup
        cleaned = textcleanup(output, line_threshold=50)
    
        # f = open('txtout_h2t/'+str(counter+1)+domain+'.txt', 'wb')
        f = open('txtout_h2t/'+str(counter+1)+'.txt', 'wb')
        f.write(line)
        f.write(cleaned)
        f.close()

    except:
        print 'html2text error ', line
        pass



    ###################################
    # html2text using lxml
    #
    try:
        htmltree = lxml.html.parse(urlopen(line))
    except IOError:
        print 'cannot open: ', line
        pass
    # html2txt
    # Ignore any characte that is not ascii coded
    try:
        output = html2txt(htmltree).encode('ascii', 'ignore')
        print 'lxml: ', line
    except:
        print 'lxml error ', line
        continue

    # cleanup
    cleaned = textcleanup(output, line_threshold=50)

    # f = open('txtout_lxml/'+str(counter+1)+domain+'.txt', 'wb')
    f = open('txtout_lxml/'+str(counter+1)+'.txt', 'wb')
    f.write(line)
    f.write(cleaned)
    f.close()


print 'All done!'
print '%i urls' % (counter+1)