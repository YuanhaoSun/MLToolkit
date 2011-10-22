#!/usr/bin/python
#
# This program stores urls from Google search results on a keyword.
#
import time, random
from xgoogle.search import GoogleSearch, SearchError

for i in range(5, 100, 5):
    
    f = open('pp'+str(i)+'.txt','wb')
    
    for j in range(i-5,i):
        wt = random.uniform(1.5, 3.5)
        gs = GoogleSearch("privacy policy")
        gs.results_per_page = 10
        gs.page = j
        results = gs.get_results()
        #Try not to annnoy Google, with a random short wait
        time.sleep(wt)
        print 'This is the %dth iteration and waited %f seconds' % (j, wt)
        for res in results:
            f.write(res.url.encode("utf8"))
            f.write("\n")
    print 'Page %d to %d done' % (i-4,i)
    f.close()
    
    #Wait few more seconds for every 50 urls
    time.sleep(random.uniform(3, 5))

print "All done"