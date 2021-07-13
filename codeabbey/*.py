def sums(n):
    ans = []
    for i in range(n):
        num = raw_input().split(' ')
        sum = 0
        for j in range(2):
            sum+=num[i]
        ans.append(str(sum))
    print(' '.join(ans))

sums(input())
