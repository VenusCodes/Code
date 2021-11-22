#https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
    if len(A) <= 2: return False
    if A[0] > A[1]: return False

    increasing = True
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            if not increasing: return False
        elif A[i] < A[i - 1]:
            increasing = False
        else:
            return False

    return not increasing

array = [0,3,2,1]
print(validMountainArray(array))