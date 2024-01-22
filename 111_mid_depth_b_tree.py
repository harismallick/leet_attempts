## 111. Minimum Depth of Binary Tree
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# Difficulty: Easy
# DFS to calculate height of tree. Return shortest height.
# Problem with this approach: how to restrict the root node from being considered a leaf node?
# If root node has no left/right child, the recursive min depth approach will always return 1.
# Can't make this work.

# Option 2: Queue based BFS - Level order traversal
# Solution accepted and beats 98% of submissions

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:

    # def minHeight(node):
    #     if node is None:
    #         return 0
        
    #     lheight = minHeight(node.left)
    #     rheight = minHeight(node.right)

    #     return 1 + min(rheight, lheight)
    
    # left_min: int = minHeight(root.left)
    # right_min: int = minHeight(root.right)

    # if left_min == 0:
    #     return right_min + 1
    # elif right_min == 0:
    #     return left_min + 1
    # else:
    #     return (min(left_min, right_min)) + 1

    # Option 2:
    if root is None:
        return 0
    queue: list = []
    i: int = 1
    queue.append((root, i))
    # print(queue)
    while len(queue) > 0:
        current_node, node_level = queue.pop(0)
        if current_node.left is None and current_node.right is None:
            return node_level
        
        if current_node.left is not None:
            queue.append((current_node.left, node_level+1))
        
        if current_node.right is not None:
            queue.append((current_node.right, node_level+1))




if __name__ == '__main__':
    # case 1:
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    # case 2:
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)

    print(minDepth(root))