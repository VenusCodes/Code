out = []
x,y = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
count = -1
prev = data[0]
for i in data:
	if i==prev:
		count+=1
	else:
		prev = i
		out.append(count+1)
		count=0
out.append(count+1)
print(*out)