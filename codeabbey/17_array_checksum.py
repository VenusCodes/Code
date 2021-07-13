x = int(input())
data = list(map(int,input().split()))
result = 0
for i in data:
	result+=i
	result*=113
	result%=10000007
print(result)