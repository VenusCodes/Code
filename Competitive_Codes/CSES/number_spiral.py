# calculate the element at a particular position
t = int(input()) 
list = [] 
while(t>0): 
	x,y = map(int, input().split()) 
	t -= 1
	if y>x :
		if y%2==0:
			ans = (y-1)*(y-1)+1+ (x-1)
		else:
			ans = y*y - (x-1)
	else:
		if x%2==1:
			ans = (x-1)*(x-1)+1+ (y-1)
		else:
			ans = x*x - (y-1)
	list.append(ans)
print(*list,sep = "\n")