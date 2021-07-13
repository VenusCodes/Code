x = int(input())
a = []
for i in range(0,x):
    string = input()
    string = string.lower()
    a.append(string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') + string.count('y'))
print(*a)