## Balanced Binary Tree
'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

# Difficulty: Easy
# DFS both sides of the tree. Compare heights. Return boolean.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    
    if root is None:
        return True
    
    def height(node):
        if node is None:
            return 0
        lheight: int = height(node.right)
        rheight: int = height(node.left)
        if lheight == -1 or rheight == -1 or abs(lheight - rheight) >= 2:
            return -1
        return 1 + max(lheight, rheight)
    
    return height(root) != -1

    
    
if __name__ == '__main__':
    # test1:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # test2:
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(4)
    print(isBalanced(root))

    # test = 0
    # if test in [0,1]:
    #     print("this syntax works.")