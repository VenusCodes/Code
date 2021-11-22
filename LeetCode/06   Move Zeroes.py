#  Move Zeroes
#https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3157/
def movezero(A: list[int]):
    count = A.count(0)
    while 0 in A:
        A.remove(0)
    A.extend([0]*count)
    print(A)

nums = [0,1,0,3,12]
nums2 = [0]
print(movezero(nums))
print(movezero(nums2))