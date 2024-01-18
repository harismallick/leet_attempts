## 100. Same Tree
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

# Difficulty: Easy

# To save on computation, no need to traverse whole trees and compare both.
# Traverse based on level. If nodes on a level identical, then progress to the next level.
# Return true if full trees traversed via BFS. Return false if not.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    if p is None and q is None:
        return True
    
    if p is not None and q is None:
        return False
    elif q is not None and p is None:
        return False
        
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
    return False


if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)
    node2 = TreeNode(1)
    node2.left = TreeNode(2)
    node2.right = TreeNode(3)

    output = isSameTree(node1, node2)
    print(output)