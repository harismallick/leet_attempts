## 112. Path Sum
'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# Difficulty: Easy

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False
    
    def searchSum(root: Optional[TreeNode], targetSum: int, currentSum=0) -> bool:
        if root is None:
            return False
        if currentSum > targetSum:
            return False
        
        if root.left is None and root.right is None:
            currentSum += root.val
            if currentSum == targetSum:
                return True
        
        left = searchSum(root.left, targetSum, currentSum=currentSum+root.val)
        right = searchSum(root.right, targetSum, currentSum=currentSum+root.val)
        return left or right
    
    
    return searchSum(root, targetSum)


if __name__ == '__main__':
    # test 1:
    # [5,4,8,11,null,13,4,7,2,null,null,null,1]
    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(8)
    # root.left.left = TreeNode(11)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(1)

    # case 2:
    root = TreeNode(1)
    root.left = TreeNode(2)

    print(hasPathSum(root, 1))


