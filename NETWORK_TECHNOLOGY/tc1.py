import json
import urllib.request, urllib.parse, urllib.error
import re
import xml.etree.ElementTree as ET
uh =  urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_267177.json')


"""    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)"""
#uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)


info = json.loads(data.decode)

sum = 0
for item in info:
    sum += item['count']

print(sum)