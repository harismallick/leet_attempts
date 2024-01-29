## 141. Linked List Cycle
'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    # if head is None:
    #     return False
    # nodes: list = []
    # node = head
    # while True:
    #     if node.next is None:
    #         return False
    #     if node in nodes:
    #         return True
    #     nodes.append(node)
    #     node = node.next

# This hash table solution was accepted, but it's O(N) time and O(N) space complexity.
# The challege asked for O(1) space complexity solution.
# The solution is a specific algorithm called Floyd's Cycle Finding Algorithm, also called the Tortoise and the Hare algo.
# Premise: Use two pointers -> One moving forward by 2 nodes, one by 1 node. If the faster pointer catches up to the slow one:
# This means the linked list have a cycle.
    if head is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
        
    return False
    

if __name__ == '__main__':
    # node1 = ListNode(3)
    # node2 = ListNode(2)
    # node3 = ListNode(0)
    # node4 = ListNode(-4)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    print(hasCycle(node1))
