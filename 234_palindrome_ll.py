## 234. Palindrome Linked List
'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes_list: list = []
        while head is not None:
            nodes_list.append(head.val)
            head = head.next
        left = 0
        right = len(nodes_list)-1
        while left < right:
            if nodes_list[left] != nodes_list[right]:
                return False
            left += 1
            right -= 1
        return True
# Solution beats 88%
# Challenge: Can you do it in O(1) space?
    
        # slow, fast, prev = head, head, None
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        # prev, slow, prev.next = slow, slow.next, None
        # while slow:
        #     slow.next, prev, slow = prev, slow, slow.next
        # fast, slow = head, prev
        # while slow:
        #     if fast.val != slow.val: return False
        #     fast, slow = fast.next, slow.next
        # return True
#Step 1: Floyd's cycle list algo to find the middle of the linked list.
#Step 2: Reverse the second half of the linked list such that middle points to None
#Step 3: Set 1 point to head and another to the tail. If values not equal, return false. Else, return true.
    
if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    head.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    print(solution.isPalindrome(head))
