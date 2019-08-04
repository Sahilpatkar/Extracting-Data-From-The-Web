import json
import urllib.request, urllib.parse, urllib.error
import re
#import xml.etree.ElementTree as ET

response =  urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_267177.json')

#response = urllib.request.urlopen(url)

data = json.loads(response.read())

#print (data)
sum = 0
for item in data['comments']:
	sum += int(item['count'])

print(sum)