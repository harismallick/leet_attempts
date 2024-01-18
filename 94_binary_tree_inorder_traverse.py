## 94. Binary Tree Inorder Traversal
'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Difficulty: Easy

# This is a DFS traversal technique for binary trees.
# Solution accepted which beats 94.63% of submissions.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root) -> list[int]:

    eg_list = []

    def recursive_dfs(root):
        if root:
            recursive_dfs(root.left)

            # print(root.val, end=" ")
            eg_list.append(root.val)

            recursive_dfs(root.right)

    
    recursive_dfs(root)

    return eg_list
    

if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    output = inorderTraversal(root)
    print(output)