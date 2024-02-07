## 222. Count Complete Tree Nodes
'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
'''
# Difficulty: Easy
# Calculate height of tree, then bfs count nodes on last layer. Then add to 2^(h-1)-1

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    def calculate_height(node):
        if node is None:
            return 0
        l_height = calculate_height(node.left)
        r_height = calculate_height(node.right)

        return 1 + max(l_height, r_height)
    tree_height: int = calculate_height(root)

    node_count = 0
    def count_nodes_at_level(root, height):
        if root is None:
            return 0
        if height == 1:
            nonlocal node_count
            node_count += 1

        else:
            count_nodes_at_level(root.left, height-1)
            count_nodes_at_level(root.right, height-1)
            
    count_nodes_at_level(root, tree_height)
    total_nodes = ((2 ** (tree_height-1))-1) + node_count

    return total_nodes

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(countNodes(root))