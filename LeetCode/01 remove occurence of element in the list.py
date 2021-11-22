#https://leetcode.com/explore/featured/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
def removeElement(nums: [int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

def removeE(nums: [int], val: int) -> int:
    a = []
    for i in nums:
        if i == val:
            pass
        else:
          a.append(i)  
        nums = a
        print(nums)
        return len(nums)
    
array = [0,4,4,0,4,4,4,0,2]
element = 4

print(removeElement(array, element))
print(array)
