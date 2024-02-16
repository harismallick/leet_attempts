## 303. Range Sum Query - Immutable
'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

'''

class NumArray:

    # def __init__(self, nums: list[int]):
    #     self.nums = nums


    # def sumRange(self, left: int, right: int) -> int:
    #     arr_sum: int = 0
    #     for i in range(left, right+1):
    #         arr_sum += self.nums[i]

    #     return arr_sum
    
    # This solution invovles calculating the sum each time in O(N) time. So, solution took 2000 ms.
    # Optimal solution is 68 ms
    # This is achieved by pre-calculating the sum of elements at each index position. Then returning difference of sums in O(1) time.
    def __init__(self, nums: list[int]):
        self.presum = nums
        for i in range(0, len(nums)-1):
            self.presum[i+1] += self.presum[i]


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.presum[right]

        return self.presum[right] - self.presum[left-1]
    
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.presum)
    print(obj.sumRange(0,2))
    print(obj.sumRange(2,5))
    print(obj.sumRange(0,5))
