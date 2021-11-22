#https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

def checkIfExist(arr: list[int]) -> bool:
    count = arr.count(0)
    if count==1:
        arr.remove(0)
    for i in arr:
        for j in arr:
            if j*2 == i:
                return True
    return False




array = [-2,0,10,-19,4,6,-8]
print(checkIfExist(array))