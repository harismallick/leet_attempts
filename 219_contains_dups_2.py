## 219. Contains Duplicate II
'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''
# Difficulty: Easy

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    num_index_map: dict = {}
    i = 0
    while i < len(nums):
        if nums[i] not in num_index_map:
            num_index_map[nums[i]] = i
        elif nums[i] in num_index_map:
            if i - num_index_map[nums[i]] <= k:
                return True
            else:
                num_index_map[nums[i]] = i
        i += 1
    return False

# Beats 98% of submissions.

if __name__ == '__main__':
    print(containsNearbyDuplicate([1,0,1,1], 1))
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))