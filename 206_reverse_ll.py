## 206. Reverse Linked List
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    ## Recursive solution:
    nodes_list: list = []
    new_head = None
    def nodes_stack(node):
        if node is None:
            return None
        nodes_list.append(node)
        nodes_stack(node.next)
        nonlocal new_head
        if new_head is None:
            new_head = nodes_list[-1]
        node = nodes_list.pop()
        # print(node.val)
        if len(nodes_list) != 0:
            node.next = nodes_list[-1]
        else:
            node.next = None
    temp_node = nodes_stack(head)
    # print(new_head.val)
    return new_head

# Recursive solution beats 84% of submissions

    ## iterative solution:
    # if head is None:
    #     return None
    # nodes_list: list = []
    # while head is not None:
    #     nodes_list.append(head)
    #     head = head.next

    # new_head = nodes_list.pop()
    # temp_node = new_head
    # while nodes_list:
    #     temp_node.next = nodes_list[-1]
    #     temp_node = nodes_list.pop()

    # temp_node.next = None

    # return new_head

# Iterative solution beats 80% of submissions


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    new_head = reverseList(node1)
    # print(new_head.val)
    while new_head is not None:
        print(new_head.val)
        print(new_head.next)
        new_head = new_head.next
