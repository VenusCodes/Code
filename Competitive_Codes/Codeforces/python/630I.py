#codeforces 630-I parking lot
# use binary exponentaion

def binpow(a,n):
    A = a
    N = n
    res = 1
    while N > 0:
        if N % 2 == 0:
            A = (A * A)
            N = N/2
        else:
            res = (A * res)
            N = N - 1
    return res

n = int(input())
print(2*4*3*binpow(4,n-3) + (n-3)*4*binpow(3,2)*binpow(4,n-4))
