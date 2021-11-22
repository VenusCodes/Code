n = int(input())
thelist = list(map(int,input().split()))[:n]
count = 0
maxi = 0
ta = thelist[0]
for i in range(1,len(thelist)):
	if thelist[i] <= 2*ta:
		count +=1;
		maxi = max(maxi,count)
	else:
		count = 0
	ta = thelist[i]
print(maxi+1)