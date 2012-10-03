#!/usr/bin/env python

# Python script to check a if a domain is down against http://www.downforeveryoneorjustme.com/google.com
# Coded by: bostonlink
# 10/9/2012

import sys, urllib2
from optparse import OptionParser

# generating help options using the OptionParser function in the optparse module

usage = """\n
Checks status of a website against www.downforeveryoneorjustme.com
usage = ./downfor.py [options] domain
author = bostonlink
"""

parser = OptionParser(usage=usage)
parser.add_option("-f", action="store", dest="filename", help="filename that contains multiple domains", metavar="Domain List")
parser.add_option("-s", action="store", dest="single", help="use for single domain check", metavar="domain")
(options, args) = parser.parse_args()

domain = sys.argv[1]

def check(domain):
    check = 'http://www.downforeveryoneorjustme.com/'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2'

    req = urllib2.Request(check + domain, headers={'User-Agent': user_agent})
    resp = urllib2.urlopen(req)

    body = resp.read()

    print "\nwww.downforeveryoneorjustme.com says:"

    if "It's not just you!" in body:
  	print "It's not just you! %s looks down from here.\n" % domain
    elif "It's just you." in body:
	print "It's just you. %s is up.\n" % domain
    else:
	print "Something went wrong check domain and try again!"

if options.single:
    
    try:
        check(domain)
    except:
	print "Something went wrong.  Check the domain name and try again"

elif options.filename:
    
    f = open(options.filename, 'r')
    for domain in f:
	d = domain.strip()
        try:
	    check(d)
	except:
	    print "Something went wrong.  Error checking %s" % d
