out = []
x = int(input())
for i in range(0,x):
	data = list(map(int,input().split()))
	data.remove(0)
	length = len(data)
	sum = 0
	for n in data:
		sum += n
	out.append(round(sum/length))
print(*out)