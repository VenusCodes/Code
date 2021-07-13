a = True
x=1
y=0
sum =0
while True:
	y,x = x,x+y
	print(x)
	if x<4000000 and x%2==0:
		sum +=x
	elif x> 4000000:
		a = False
		break

print(sum)