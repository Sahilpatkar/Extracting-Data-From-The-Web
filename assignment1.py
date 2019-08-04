import re

text_file = open("sample1.txt","r")

x = text_file.read()


text_file.close()

y = re.findall('[0-9]+',x)


m = 0
for i in y:
	int_i = int(i)
	m += int_i

print(m)



	

