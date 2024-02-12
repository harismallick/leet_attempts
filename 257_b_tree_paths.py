## 257. Binary Tree Paths
'''

'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if root is None:
            return []
        root_to_leaves: list = []

        def traverse_tree(node: Optional[TreeNode], node_path: str):
            if node is None:
                return
            path = node_path + str(node.val) + "->"
            if node.left is None and node.right is None:
                output = path[0:-2]
                if output not in root_to_leaves:
                    return root_to_leaves.append(output)
                return
            if node.left:
                traverse_tree(node.left, path)
            if node.right:
                traverse_tree(node.right, path)
        traverse_tree(root, "")
        return root_to_leaves
    
# Beats 80% of submissions.
    
if __name__ == '__main__':
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(5)
    output = Solution()
    print(output.binaryTreePaths(root))
