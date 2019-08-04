import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

url = input('ENTER - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

counts = []
tags = soup('span')
for tag in tags:
	 print(tag.contents[0])
	 counts.append(tag.contents[0])

	
m = 0
for i in counts:
	int_i = int(i)
	m += int_i

print(m)	




'''
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs'''