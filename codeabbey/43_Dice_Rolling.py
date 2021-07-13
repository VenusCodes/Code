out = []
x = int(input())
for i in range(0,x):
	n = float(input())
	n*=6;
	n+=1;
	out.append((int)(n))
print(*out)