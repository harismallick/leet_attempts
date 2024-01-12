## 35. Search Insert Position

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

# Difficulty: Easy
# Solution: Binary search algorithm as it O(log n)

def searchInsert(nums: list[int], target: int) -> int:

    start: int = 0
    end: int = len(nums)-1
    index: int = 0
    while start <= end:
        middle: int = (start + end) // 2
        # print(middle)
            
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            index = middle
            start = middle + 1
        elif target < nums[middle]:
            index = middle
            end = middle - 1
    # print(f"The index is: {index}")
    return start # simpler that what I did
# What I did:
    # if nums[index] < target:
    #     return index + 1
    # if nums[index] > target:
    #     return index

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3], 0))
print(searchInsert([1,3], 2))
print(searchInsert([3,5,7,9,10], 8))



