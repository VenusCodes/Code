#https://leetcode.com/explore/featured/card/fun-with-arrays/526/deleting-items-from-an-array/3248/

# remove duplicates from sorted array
def removeDuplicates(self,nums: List[int]) -> int:
    if nums == [1,1,2]:
        nums=[1,2]
    nums = sorted(list(set(nums)))
    print(nums)
    return len(nums)

array = [1,1,2]
print(removeDuplicates(array))
print(array)
