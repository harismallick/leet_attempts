## 108. Convert Sorted Array to Binary Search Tree
'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
'''

# Difficulty: Easy
# A BST is created on an array of sorted elements.
# The left-most leaf node is the smallest value.
# Right-most leaf node is the largest value.
# Learn how to convert a sorted array into a BST for this question.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int]) -> Optional[TreeNode]:

    if not nums:
        return None
    
    middle: int = len(nums) // 2
    root: Optional[TreeNode] = TreeNode(nums[middle])

    root.left = sortedArrayToBST(nums[:middle])
    root.right = sortedArrayToBST(nums[middle+1:])
    
    return root

if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    root = sortedArrayToBST(nums)
    while root.left is not None:
        print(root.left.val)
        print(root.right.val)
        root = root.left