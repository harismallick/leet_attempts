## 268. Missing Number
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # if nums == [] or nums == [1]:
        #     return 0
        # elif nums == [0]:
        #     return 1
        # largest_num: int = 0
        # zero_present: bool = False
        # for num in nums:
        #     if num == 0:
        #         zero_present = True
        #     if num > largest_num:
        #         largest_num = num
        # if zero_present:
        #     for i in range(1, largest_num+2):
        #         if i not in nums:
        #             return i
        # return 0
# Solution is O(2N) time and O(1) space so meets the requirements of the task. But the solution is slow. Only beats 10% of submissions.
        list_sum: int = 0
        true_sum: int = 0
        for i in range(0, len(nums)):
            list_sum += nums[i]
            true_sum += i+1

        return true_sum - list_sum
    
# This second solution faster than 97% of submissions.
    
if __name__ == '__main__':
    nums: list = [3,0,1]
    # nums = [9,6,4,2,3,5,7,0,1]
    # nums = [1,1,1,1,1,2,3,4,5]
    output = Solution()
    print(output.missingNumber(nums))