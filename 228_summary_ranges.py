## 228. Summary Ranges
'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''
# Difficulty: Easy

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        previous_num: int = nums[0]
        range_start: int = nums[0]
        output: list[str] = []
        for i in range(1, len(nums)):
            if (nums[i] - previous_num > 1):
                if range_start < previous_num:
                    output.append(f"{range_start}->{previous_num}")
                else:
                    output.append(str(previous_num))
                range_start = nums[i]
            
            if i == len(nums)-1:
                if range_start < nums[i]:
                    output.append(f"{range_start}->{nums[i]}")
                else:
                    output.append(str(nums[i]))

            previous_num = nums[i]
        return output
# Solution beats 72% of submissions.
    
if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    # nums = [0,2,3,4,6,8,9]
    solution = Solution()
    print(solution.summaryRanges(nums))