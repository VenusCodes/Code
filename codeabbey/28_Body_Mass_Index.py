out = []
x = int(input())
for i in range(0,x):
	w,h = map(float,input().split())
	bmi = w / (h*h)
	if bmi<18.5:
		out.append("under")
	elif 18.5<=bmi<25.0:
		out.append("normal")
	elif 25.0<=bmi<30.0:
		out.append("over")
	else:
		out.append("obese")
print(*out)