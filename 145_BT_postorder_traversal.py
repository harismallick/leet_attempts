## 145. Binary Tree Postorder Traversal
'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: Optional[TreeNode]) -> list[int]:
    nodes_list: list[TreeNode] = []
    def dfs_recursive(node):
        if node:
            dfs_recursive(node.left)
            dfs_recursive(node.right)
            nodes_list.append(node.val)
        
    dfs_recursive(root)
    return nodes_list

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(postorderTraversal(root))