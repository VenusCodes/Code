#
#		these solution is not working for testcase 5
##
n = int(input())
thelist = list(map(int,input().split()))[:n]
thelist2 = sorted(thelist)
count = 0
address = []
if len(thelist) <= 2:
	print('yes\n')
else:
	for i in range(len(thelist)):
		if thelist[i] != thelist2[i]:
			count += 1
			address.append(thelist[i])
	if count==2:
		print('yes')
		print(*sorted(address))
	else:
		print('no')