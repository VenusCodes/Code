n = int(input())
#thelist = list(int(element) for element in input().strip().split(" "))[:n]
thelist = list(map(int,input().strip().split()))[:n]
a,b = map(int,input().strip().split())
print(sum(thelist[a:b+1]))