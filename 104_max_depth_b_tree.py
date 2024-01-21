## 104. Maximum Depth of Binary Tree
'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Difficulty: Easy

# To calculate the height of tree, must do DFS.
# Keep track of longest distance from root to leaf.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    # height = 1
    # if root is None:
    #     return 0
    # return height + max(maxDepth(root.left), maxDepth(root.right))

    # alternative way to write the code:
    if root is None:
        return 0
    lheight: int = maxDepth(root.left)
    rheight: int = maxDepth(root.right)
    return 1 + max(lheight, rheight)

# My solution faster than 65% of submissions
# This solution faster than 83.2%

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(maxDepth(root))