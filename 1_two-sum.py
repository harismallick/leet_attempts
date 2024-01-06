# Difficulty: Easy
# Challenge: Use an algorithm better than O(n^2) 

## My solution:

# def twoSum(nums: list[int], target: int) -> list[int]:
#     nums_dict: dict = {}

#     for i, num in enumerate(nums):
#         if num not in nums_dict.keys():
#             nums_dict[num] = [i]
#         else:
#             nums_dict[num].append(i)
#     # print(nums_dict)
#     for num in nums:
#         difference = target - num
        
#         if difference in nums_dict.keys():

#             if difference == num:
#                 if len(nums_dict[num]) == 1:
#                     continue

#             num_index = nums_dict[num].pop()
#             difference_index = nums_dict[difference].pop()
#             return [num_index, difference_index]

#     return "No result found."

## More optimal solution: 
# Dont create complete hash map from the start. Add elements to hash map while
# iterating though the array ONLY once.

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_dict: dict = {}

    for i, num in enumerate(nums):
        difference = target - num
        
        if difference in nums_dict.keys():
            difference_index = nums_dict[difference].pop()
            return [difference_index, i]
        else:
            nums_dict[num] = [i]

    return "No result found."

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

