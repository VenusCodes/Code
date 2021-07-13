a = []
input = list(map(int,input().split()))
input.pop(0)
for f in input:
	c = (f-32)*5/9
	a.append(round(c))
print(*a)