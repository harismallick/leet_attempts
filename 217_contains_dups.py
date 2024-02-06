## 217. Contains Duplicate
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''
# Difficulty: Easy

def containsDuplicate(nums: list[int]) -> bool:
    num_seen: dict = {}

    for num in nums:
        if num not in num_seen:
            num_seen[num] = 1
        elif num in num_seen:
            return True
    return False

if __name__ == '__main__':
    print(containsDuplicate([1,2,3,1]))