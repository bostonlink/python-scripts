#!/usr/bin/env python

# PCAP parser that parses HTTP packets the data within sessions using scapy
# This script was written for a malware investigation of the Gozi botnet
# Gozi uses the HTTP POST to upload intercepted user sessions from the compromised host.

# Author : bostonlink
# Usage : ./script.py file.pcap

import sys
from scapy.all import *
# note this script depends on scapy being installed on the system

pcap_in = sys.argv[1]

pcap = rdpcap(pcap_in)

for pkt in pcap:

    raw_data = pkt.sprintf("%Raw.load%")

    if "Content-Disposition:" and "URL:" in raw_data:
        
	print pkt.summary() + "\n"

        data = str(raw_data).lstrip("'").rstrip("'").split("\\r\\n")
        
	for line in data:
           print line
        
	print "#" * 100
	print "\n"
