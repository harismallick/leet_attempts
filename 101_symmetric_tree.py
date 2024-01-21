## 101. Symmetric Tree
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Difficulty: Easy

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:

    def symmetry_check(left, right):
        if left is None and right is None:
            return True
        
        elif left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left.val != right.val:
            return False
        else:
            return symmetry_check(left.left, right.right) and symmetry_check(left.right, right.left)
    
    return symmetry_check(root.left, root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(isSymmetric(root))