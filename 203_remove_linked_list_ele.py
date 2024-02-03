## 203. Remove Linked List Elements
'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    node = head
    previous_node = None
    while node is not None:
        if node.val == val:
            if previous_node is not None:
                previous_node.next = node.next
                node = node.next
            
            else:
                head = node.next
                node = head

        else:
            previous_node = node
            node = node.next
    return head
# This solution beats 65% of submissions.
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(6)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node = removeElements(node1, 6)
    print(node)
    while node is not None:
        print(node.val)
        node = node.next
