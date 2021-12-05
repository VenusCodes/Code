def solution(n):
    return 2*sum((1+2*i) for i in range(n-1)) + (1+2*(n-1))

print(solution(1))
print()
print(solution(2))
print()
print(solution(3))
print()
print(solution(4))

# 1 2 3  4
# 1 5 13 25
# 1 3 5 7 
