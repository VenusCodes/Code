n,L,a = map(int,input().strip().split())
t = []
l = []
for i in range(n):
	temp1 , temp2 = map(int,input().strip().split())
	t.append(temp1)
	l.append(temp2)

start = 0
answer = 0
for i in range(n):
	answer += int((t[i]-start)/a)
	start = t[i]+l[i]
answer += int((L - start)/a)
print(answer)






# answer = 0
# if n!=0:
# 	for i in range(n):
# 		temp1 , temp2 = map(int,input().strip().split())
# 		t.append(temp1)
# 		l.append(temp2)
# 	answer += int(t[0]/a)
# 	print(answer)
# 	for i in range(n-1):
# 		gap = t[i+1] - (t[i]+ l[i])
# 		print(gap)
# 		answer += int(gap/a)
# 		print(answer)
# 	answer += int((L - t[n-1] + l[n-1])/a)
# 	print(answer)
# else:
# 	print(int(L/a))