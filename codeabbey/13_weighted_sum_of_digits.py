out = []
x = int(input())
data = list(map(int,input().split()))
for num in data:
	a = []
	while (int)(num)>0:
		a.append(int(num%10))
		num/=10
	posi = len(a)
	sum = 0
	for j in a:
		sum += posi*j;
		posi-=1
	out.append(sum)
print(*out)