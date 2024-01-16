## 88. Merge Sorted Array
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the 
array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote 
the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.
'''

# Difficulty: Easy

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:

    # if n == 0:
    #     return nums1
    # if m == 0:
    #     nums1.clear()
    #     for num in nums2:
    #         nums1.append(num)
    #     return nums1
    # for pop in range(0, n):
    #     nums1.pop()
    
    # i: int = 0
    # j: int = 0
    # while j < n:

    #     if nums2[j] <= nums1[i]:
    #         nums1.insert(i, nums2[j])
    #         j += 1
    #     elif i == len(nums1)-1:
    #         nums1.append(nums2[j])
    #         i += 1
    #         j += 1

    #     else:
    #         i += 1
    # return nums1

## Faster solution using 'three' pointers, not 2:
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([1,0], 1, [2], 1))
print(merge([4,5,6,0,0,0], 3, [1,2,3], 3))
print(merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))

