string = input().strip().lower()
string = string.replace("a",'')
string = string.replace("o",'')
string = string.replace("y",'')
string = string.replace("e",'')
string = string.replace("u",'')
string = string.replace("i",'')
string2 = ''
for i in string:
	string2 = string2+ '.' + i
print(string2)