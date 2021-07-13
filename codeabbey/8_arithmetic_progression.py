out = []
x = int(input())
for i in range(0,x):
	a,d,n = map(int,input().split())
	sum =(n/2)*(2*a + (n-1)*d)
	out.append(int(sum))
print(*out)