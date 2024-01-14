## 83. Remove Duplicates from Sorted List
'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

# Difficulty: Easy

class ListNode():
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution():
    # def __init__(self, nodes: list):
    #     self.head = None
    #     if nodes is not None:
    #         node = ListNode(val=nodes.pop(0))
    #         self.head = node

    #         for item in nodes:
    #             node.next = ListNode(val=item)
    #             node = node.next

    # def __repr__(self) -> str:
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append(str(node.val))
    #         node = node.next

    #     nodes.append("None")
    #     return "->".join(nodes)
    
    def deleteDuplicates(self, head):

        current_node = head
        unique_node = current_node

        while current_node is not None:
            if current_node.val != unique_node.val:
                unique_node.next = current_node
                unique_node = current_node

            current_node = current_node.next

            if current_node is None:
                unique_node.next = None
         
        return head
    
# ll1 = Solution([1,1,2])
# print(ll1)
node1 = ListNode(val=1)
node2 = ListNode(val=1)
node3 = ListNode(val=2)
node4 = ListNode(val=3)
node5 = ListNode(val=3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# print(node2.next.val)
test = Solution()
test.deleteDuplicates(node1)

test_node = node1
while test_node is not None:
    print(test_node.val)
    test_node = test_node.next
