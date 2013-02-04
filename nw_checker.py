#!/usr/bin/env python

# Script to check a list of IP addresses or Domain names and see if they are in the NW DB 
# Author: David Bressler
# Date: 1/25/2013

import sys
import json
import urllib, urllib2

def nw_http_auth(nwa, nwusr, nwpass):

	"""Authenticates to the NW REST API via HTTP Basic authentication"""
	try:
		auth_handler = urllib2.HTTPBasicAuthHandler()
		auth_handler.add_password(realm = 'NetWitness',
								uri = nwa,
								user = nwusr,
								passwd = nwpass )

		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)
	except Exception as e:
		print 'Authentication Failed: %s' % e

def nwQuery(nwa, id1, id2, query_string, cType, size):

	""" Queries the NW REST API and returns the results 
	Example query that would be passed to the function in the query_string variable:
	query = 'select service,ip.src,country.dst where service=80'"""

	base_uri = "/sdk?msg=query&"
	params_dic = { 'force-content-type': cType, 'expiry': 600, 'id1': id1, 'id2': id2, 'size': size, 'query': query_string}
	enc_params = urllib.urlencode(params_dic)
	full_url = nwa + base_uri + enc_params
	try:
		req = urllib2.Request(full_url)
		ret = urllib2.urlopen(req)
		ret_data = ret.read()
		return ret_data
	except urllib2.HTTPError as e:        
		print 'The API HTTP Request had the following error %s' % e
		sys.exit(0)

nwa = 'http://10.36.129.90:50105'
nwusr = 'dbressler'
nwpass = 'p@ssw0rd'
nw_http_auth(nwa, nwusr, nwpass)

f = open(sys.argv[1], 'r')
hostlist = f.readlines()
f.close()

out = open('results.txt', 'w')

for l in hostlist:
	l = l.strip()
	query = 'select ip.dst where ip.dst=%s' % l
	json_data = json.loads(nwQuery(nwa, 0, 0, query, 'application/json', 10))
	results_list = []
	for l in json_data['results']['fields']:
		if l['value'] not in results_list:
			print '%s is in the NW Database' % l['value']
			out.write('%s is in the NW Database\n' % l['value'])
			results_list.append(l['value'])

print '\nScript Completed and output stored to results.txt in the CWD'
out.close()