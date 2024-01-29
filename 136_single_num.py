## 136. Single Number
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
# While my solution of appending to a list and removing duplicates was accepted, it was not the fastest solution.
# The fastest solution is to perform bit manipulation, by using the XOR operator.
# Need to learn more about bit manipulation.

def singleNumber(nums: list[int]) -> int:
    # count: dict = {
    #     "1": []
    # }
    # for num in nums:
    #     if num not in count["1"]:
    #         count["1"].append(num)
    #     elif num in count["1"]:
    #         count["1"].remove(num)
    
    # return count["1"][0]
    xor = 0
    for num in nums:
        xor ^= num

    return xor

if __name__ == '__main__':
    # print(singleNumber([2,2,1]))
    print(singleNumber([4,1,2,1,2]))
    # print(singleNumber([1]))