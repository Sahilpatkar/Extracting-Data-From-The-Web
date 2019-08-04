import urllib.request, urllib.parse, urllib.error
import re

fhand =  urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_267177.json')

counts = []
for line in fhand:
	x = line.decode().strip()
	for i in x:
		counts.append(i)

	

y = re.findall('[0-9]+',counts)


m = 0
for i in y:
	int_i = int(i)
	m += int_i
print(y)
print(m)	

#https://en.wikipedia.org/wiki/Main_Page