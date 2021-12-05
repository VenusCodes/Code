string = list(int(x) for x in input().strip())
count = string.count(4)+string.count(7)
if count ==4 or count == 7:
	print('YES')
else:
	print('NO')