## 283. Move Zeroes
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
from typing import Optional

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(set(nums)) == 1:
        #     return
        # i: int = 0
        # j: int = len(nums)-1
        # while i < j:
        #     if nums[i] == 0:
        #         zero: int = nums.pop(i)
        #         nums.append(zero)
        #         j -= 1
        #     else:
        #         i += 1

        # return None
# Solution accepted but only beats 30% of submissions: 137 ms
    
# Faster solution that doesn't involve popping elements out from the array; move all encountered 0s down the array together:
        if len(set(nums)) == 1:
            return
        
        snowball_size: int = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                snowball_size += 1
            
            elif snowball_size > 0:
                temp: int = nums[i]
                nums[i] = 0
                nums[i-snowball_size] = temp
        return
# This solution faster than 65% of submissions, but its only 9 ms faster! 128 ms
if __name__ == '__main__':
    output: Optional[Solution] = Solution()
    given_list: list = [0,1,0,3,12]
    output.moveZeroes(given_list)
    print(given_list)
    test = ["cat", "cat", "dog", "mouse", "dog"]
    print(set(test))