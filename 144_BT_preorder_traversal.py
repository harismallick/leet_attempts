## 144. Binary Tree Preorder Traversal
'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
    nodes_list: list[TreeNode] = []

    def dfs_recursive(node):
        if node:
           nodes_list.append(node.val)
           dfs_recursive(node.left)
           dfs_recursive(node.right)
    dfs_recursive(root) 
    return nodes_list

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(preorderTraversal(root))