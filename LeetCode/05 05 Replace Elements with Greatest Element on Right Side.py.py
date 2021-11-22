#https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3259/
def replaceelement(A: list[int]):
    A.append(-1)
    for i in range(len(A)-1):
        A[i]=max(A[i+1:])
    A.pop(-1)
    print(A)
    
arr = [400]
print(replaceelement(arr))