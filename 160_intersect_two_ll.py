## 160. Intersection of Two Linked Lists
'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:

    first_ll: set[ListNode] = set()
    node_first_ll = headA

    while node_first_ll is not None:
        first_ll.add(node_first_ll)
        node_first_ll = node_first_ll.next

    node_second_ll = headB
    while node_second_ll is not None:
        if node_second_ll in first_ll:
            return node_second_ll
        node_second_ll = node_second_ll.next

    return None

# Solution accepted and beats 80%
# Alternative solution: 2 pointers -> reset 1 pointer at tail to the head of the other pointer.
# By traversing A+C+B+C on pointer-1 and B+C+A+C on pointer 2, if intersection point exists, it will be reached in second iteration.

if __name__ == '__main__':
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    nodeA1 = ListNode(4)
    nodeA2 = ListNode(1)
    nodeA3 = ListNode(8)
    nodeA4 = ListNode(4)
    nodeA5 = ListNode(5)
    nodeA1.next = nodeA2
    nodeA2.next = nodeA3
    nodeA3.next = nodeA4
    nodeA4.next = nodeA5
    nodeB1 = ListNode(5)
    nodeB2 = ListNode(6)
    nodeB3 = ListNode(1)
    nodeB1.next = nodeB2
    nodeB2.next = nodeB3
    nodeB3.next = nodeA3
    print(getIntersectionNode(nodeA1, nodeB1))
    