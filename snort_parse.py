#!/usr/bin/env python

# Script to search through the 'sid-msg.map' file for snort signatures and displays all information about the signature
# Author: bostonlink
# Date: 10/25/2012

import os, sys

help = """
Something went wrong try again view usage:

Usage: ./snort_parser.py [search string]
Example: ./snort_parser.py \"et malware fun web products adware agent traffic\"

Note: The snort ruleset must be in the CWD of the script and named 'rules' for the script
to be able to parse them.
"""


if len(sys.argv) != 2:
    print help
    sys.exit(0)
else:
    sig_str = sys.argv[1]

sigs = open("rules/sid-msg.map", "r")

# searching for user supplied string in sid-msg.map file
for line in sigs:
    
    diced = line.split('||')

    if sig_str.lower() in diced[1].lower():
	print "*" * 80
	print "Details of %s rule" % diced[1].lstrip()
	print "*" * 80 + "\n"
	print "Snort sid-msg.map info\n"
	print "Snort rule sid:  %s" % diced[0]
	print "Snort rule msg:  %s" % diced[1].lstrip()
	print "Snort rule refs: %s" % diced[2].lstrip()
	print "Additional info: %s" % diced[3].lstrip()

	search_str = sig_str.split()

	for file in os.listdir("rules"):
    
    	    if search_str[1] in file:
		rules = open('rules/' + file, 'r')
		print "Opening rules/%s and searching for %s\n" % (file, diced[0])

		for line in rules:
	    	    if "sid:" + diced[0].strip() in line:
		        print "Snort rule signature\n"
			print line
			break

	        rules.close()

sigs.close()
