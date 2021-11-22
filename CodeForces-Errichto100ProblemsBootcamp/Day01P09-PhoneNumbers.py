n = int(input())
thelist = list(map(int,input()))[:n]
n8 = thelist.count(8)
if n8 > 0:
	count = int(len(thelist)/11)
	if count < n8:
		print(count)
	else:
		print(n8)
else:
	print(0)