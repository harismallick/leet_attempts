## 26. Remove Duplicates from Sorted Array
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

# def remove_duplicates(nums: list) -> int:
#     k = 0

#     if len(nums) == 0:
#         return 0
#     elif len(nums) == 1:
#         return 1

#     last_num = nums[-1]
#     temp_num = None
#     i = 0
#     j = 0
#     # while temp_num is None or isinstance(temp_num, int):
#     while j <= len(nums)-1:
#         # if temp_num == "_":
#         #     break

#         if temp_num == nums[i]:
#             nums.pop(i)
#             nums.append("_")

#         elif temp_num != nums[i]:
#             temp_num = nums[i]
#             k += 1
#             i += 1

#         j += 1
#         if temp_num is None:
#             temp_num = nums[i]
#             i += 1
#             continue
#     return k

## faster solution:

def remove_duplicates(nums: list) -> int:
    
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1

    return j

list1 = [1,1]
list1 = [1,2]
# list1 = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(list1))
print(list1)