import urllib
import urllib2
import json
from pprint import pprint

'''base = 'http://maps.googleapis.com/maps/api/geocode/json'
addr = '1325 4th Ave, Seattle, WA 98101'
data = {'address': addr, 'sensor': 'false' }
query = urllib.urlencode(data)
res = urllib2.urlopen('?'.join([base, query]))
response = json.load(res)
pprint(response)


base = 'http://api.techsavvy.io/jobs'
search = 'python+web'
res = urllib2.urlopen('/'.join([base, search]))
response = json.load(res)
for post in response['data']:
	for key in sorted(post.keys()):
		print "%s:\n    %s" % (key, post[key])'''

def reverse_lookup(lat,long):
	base = 'http://maps.googleapis.com/maps/api/geocode/json'
	latlong = str(lat) + "," + str(long)
	print latlong
	data = {'latlong':latlong, 'sensor': 'false'}
	query = urllib.urlencode(data)
	print query
	res = urllib2.urlopen('?'.join([base, query]))
	response = json.load(res)
	pprint(response)

reverse_lookup(40.714224,-73.961452)



