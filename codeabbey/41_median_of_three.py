out = []
x = int(input())
for i in range(0,x):
	three = list(map(int,input().split()))
	three.remove(max(three))
	three.remove(min(three))
	out.append(three[0])
print(*out)