## 169. Majority Element
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

def majorityElement(nums: list[int]) -> int:

    # count_map: dict = {}
    # for num in nums:
    #     if count_map.get(num) is None:
    #         count_map[num] = 1
    #     else:
    #         count_map[num] += 1

    # return max(count_map, key=count_map.get)

# This could be considered the naive solution for the problem, but its space complexity is O(M), where M is number of unique elements in list.

# The O(1) space complexity solution is the Boyer-Moore Mojority Vote algorithm
# If an element occurs n/2 times in a list of size n, then this solution is best.

    count: int = 0
    candidate: int = 0
    for num in nums:
        if count == 0:
            candidate = num
        
        if candidate == num:
            count += 1
        else:
            count -= 1

    return candidate

if __name__ == '__main__':
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([3,3,4]))