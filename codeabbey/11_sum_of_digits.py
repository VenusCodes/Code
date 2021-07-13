out = []
n = int(input())
for i in range(0,n):
	a,b,c=map(int,input().split())
	num = a*b+c
	sum = 0
	for c in str(num):
		sum+=int(c)
	out.append(sum)
print(*out)