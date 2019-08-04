import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


m = 0

url = input('Enter - ')
loop = int(input("no of times to loop - ") )
pos = int(input('pos of the link in every loop - '))

while m<loop:
    m +=1    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    i = 0
    tags = soup('a')
    for tag in tags:
        i += 1
        if(i==pos):


            url = (tag.get('href', None))
            x = tag.contents[0]

print(x)
           