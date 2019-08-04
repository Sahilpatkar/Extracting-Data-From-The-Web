import json

input = '''
[
	{"name":"sahil"
	,"ID":"001"},

	{"name":"aditya"
	,"ID":"002"}
]'''

info = json.loads(input)
print("user count:",len(info))

for item in info:
	print("Name:",item['name'])
	print("ID",item['ID'])