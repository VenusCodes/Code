n = int(input())
answer =[]
for i in range(0,n):
	a = map(int,raw_input().split())
	answer.append(min(a))

print(' '.join(str(x) for x in answer))