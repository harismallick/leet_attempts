## 179. Largest Number
'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''

# Difficulty: Medium
# Attempt at solution 1:

def largestNumber(nums: list[int]) -> str:

    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(0, nums_len-1-i):
            num1 = str(nums[j])
            num2 = str(nums[j+1])

            if num1 + num2 < num2 + num1:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    if nums[0] == 0:
        return "0"
    
    return "".join(str(x) for x in nums)

# Attempt at solution 2:

# def largestNumber2(nums: list[int]) -> str:
#     string_list: list = [str(x) for x in nums]
#     num_str: str = string_list.pop(string_list.index(max(string_list)))

#     while len(string_list) != 0:
#         new_num: str = string_list.pop(string_list.index(max(string_list)))
#         temp_str1: str = num_str + new_num
#         temp_str2: str = new_num + num_str
#         if int(temp_str1) > int(temp_str2):
#             num_str = temp_str1
#         else:
#             num_str = temp_str2

#     return num_str

print(largestNumber([3,30,34,5,9]))
print(largestNumber([10, 2]))
print(largestNumber([111311, 1113]))
print(largestNumber([10,2,9,39,17]))
print(largestNumber([0,0]))
# print(max(str(1113), str(111311)))