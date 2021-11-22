n = int(input())
thelist = list(int(element) for element in input().strip().split(" "))[:n]
print(*reversed(thelist))