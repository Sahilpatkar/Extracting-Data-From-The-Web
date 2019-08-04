import re
x = 'First: 1: my 1 email id is sahil.patkar88@gmail.com'
W = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('[0-9]+',x)
z = re.findall('^F.+:',x)
c = re.findall('^F.+S:',x)
q = re.findall('\S+?@\S+',x)
r = re.findall('href="(.+)"',W)
print(y)
print(z)
print(c)
print(q)
print(r)


'''^	  Matches the beginning of a line
$	  Matches the end of the line
.	  Matches any character
\s	  Matches whitespace
\S	  Matches any non-whitespace character
*	  Repeats a character zero or more times
*?	  Repeats a character zero or more times (non-greedy)
+	  Repeats a character one or more times
+?	  Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	  Indicates where string extraction is to start
)	  Indicates where string extraction is to end'''