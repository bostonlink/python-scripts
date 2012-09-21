#!/usr/bin/env python

"""URL Puller - pulls the source and parses links from a specified website"""

import urllib2,sys

usage = '''
link_puller.py coded by: bostonlink
example: ./link_puller.py http://pentest-labs.org
'''

if len(sys.argv) != 2:
    print(usage)
    sys.exit(0)

url_html = urllib2.urlopen(sys.argv[1])
html_read = url_html.read()

for url in html_read.split():
    if 'http://' in url:
        if 'href=' in url:
            urls = url.lstrip('href=').split('>')
            for i in urls:
                if 'http://' in i:            
                    print(i.lstrip("'\"").rstrip("'\""))
    else:
        continue 


