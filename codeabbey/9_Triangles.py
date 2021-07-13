out = []
x = int(input())
for i in range(0,x):
	a,b,c = map(int,input().split())
	if((a+b > c) and (a+c>b) and (b+c>a)):
		out.append(1)
	else:
		out.append(0)
print(*out)