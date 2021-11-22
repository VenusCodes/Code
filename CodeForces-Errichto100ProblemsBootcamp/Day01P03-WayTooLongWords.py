# def func(a):
# 	if len(a)>4:
# 		a = a[0] + str(len(a)-2) + a[-1]
# 	return a

# n = int(input())
# thelist = []
# for i in range(n):
# 	string = input().strip()
# 	thelist.append(string)
# print('\n'.join(map(func,thelist)))

#the above  code gave error in test 2

n = int(input())
for i in range(n):
    s = input()
    ans = s[0] + str(len(s) - 2) + s[-1] if len(s) > 10 else s
    print(ans)