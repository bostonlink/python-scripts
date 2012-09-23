#!/usr/bin/env python

# python script to automate nmap scans of a perimeter network.
# can be modified for single IP, IP range, or IP list file.
# Coded by bostonlink @ pentest-labs.org

import subprocess, time
from optparse import OptionParser
from datetime import date

# generating help options using the OptionParser function in the optparse module

usage = """\n
nmap automated scan script, a frontend script to automate nmap scans and create cronjobs from the script.
usage = ./nmap_scan_auto.py [options] 
author = bostonlink @ pentest-labs.org
"""

parser = OptionParser(usage=usage)
parser.add_option("-f", action="store", dest="filename", help="filename that contains multiple ip ranges", metavar="IP Range List")
parser.add_option("-s", action="store", dest="single", help="use when scanning single ip or single ip range", metavar="IP Address")
parser.add_option("-d", action="store_true", dest="verbose", help="uses ndiff tool to diff nmap xml output files")
(options, args) = parser.parse_args()

# logic portion of the script, executes commands and diff two files.

if options.filename:
    inlist = open(options.filename, 'r').readlines()
    for i in inlist:
        outfilename = i.replace('.','_').strip() + '_' + str(date.today())
        subin = i.strip()    
        subprocess.Popen("nmap -sS -PN %s --reason -oA %s &" % (subin, outfilename.replace('/','_')), shell=True).wait()
        print("\nNmap scan has finished scanning the " + subin + "subnet")

if options.single:
   outfilename = 'nmapout_' + str(date.today())
   subprocess.Popen("nmap -sS -PN %s -p 0- --reason -oA %s" % (options.single, outfilename), shell=True).wait()
   print("\nNmap scan has finished see output files within the directory you ran this script in")

# if options.verbose:
       
