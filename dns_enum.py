#!/usr/bin/env python

# a script that uses the linux host command to enumerate dns information and attempt a zone transfer
# Quick and dirty automation of dns enumeration.  Probably better ways but hey next time!
# coded by: bostonlink

import sys,subprocess

usage = """dns_enum.py coded by bostonlink
Usage: ./dns_script.py [domain name]
Example: ./dns_script.py google.com"""

if len(sys.argv) != 2:
    print(usage)
    sys.exit(0)

target = sys.argv[1]

print("\n" + "*" * 60)
print("%s nameservers" % target)
print("*" * 60 + "\n")

pro1 = subprocess.Popen(["host","-t","ns",target], stdout=subprocess.PIPE)
ns = pro1.stdout.read()
pro1.wait()
print(ns)

print("\n" + "*" * 60)
print("%s mailservers" % target)
print("*" * 60 + "\n")

pro2 = subprocess.Popen(["host","-t","mx",target], stdout=subprocess.PIPE)
mx = pro2.stdout.read()
pro2.wait()
print(mx)

ns_list = ns.strip().split()
for nameserver in ns_list:
    if nameserver.endswith("."):
	zone_tr = nameserver.rstrip(".")
        print("\n" + "*" * 60)
	print("%s zone transfer against %s" % (target,zone_tr))
	print("*" * 60 + "\n")
        pro3 = subprocess.Popen(["host","-l",target,zone_tr], stdout=subprocess.PIPE)
        ztrans = pro3.stdout.read()
	pro3.wait()
	print(ztrans)
    else:
        continue

print("\nScript completed")
