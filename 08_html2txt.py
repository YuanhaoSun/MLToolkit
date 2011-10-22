import os
import lxml.html

def html2text(html):
    tree = lxml.etree.fromstring(html, lxml.etree.HTMLParser())if isinstance(html, basestring) else html 
    for skiptag in ('//script', '//iframe'):
        for node in tree.xpath(skiptag):
            node.getparent().remove(node)
    return lxml.etree.tounicode(tree, method='text') 

# link = lxml.html.parse('http://www.elsevier.com/privacypolicy')
link = lxml.html.parse('http://www.google.com/privacy/privacy-policy.html') 
# Ignore any characte that is not ascii coded 
output = html2text(link).encode('ascii', 'ignore')

f = open('google.txt', 'wb')
f.write(output)
f.close()