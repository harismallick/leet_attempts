## 21. Merge Two Sorted Lists
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
## I solved it my way. Passed the test cases. Leet not accepting answer due to object 
## attribute issues. Cba to make it work.
class Node():
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data)
    
    def node_value(self):
        return self.data
    
class LinkedList():
    def __init__(self, nodes: list=None) -> None:
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for item in nodes:
                node.next = Node(item)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")
        return "->".join(nodes)
    
    def nodes_array(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node)
            node = node.next
        return nodes
    
    def get_length(self)-> int:
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count
    
    def add_node(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        node = self.head
        new_node = Node(data)

        if index == 0:
            new_node.next = node
            self.head = new_node
            return "New head created"

        previous_node = None
        i = 0
        while i <= index:
            if i == index:
                previous_node.next = new_node
                new_node.next = node
                break
            previous_node = node
            node = node.next
            i += 1

        return f"{data} added at position {index}"
    

    def combine_sorted_lists(self, list2):
        linked_list_check = isinstance(list2, LinkedList)
        if not linked_list_check:
            raise Exception("Given list is not a linked list")
        
        current_node = self.head
        previous_node = None

        while list2.head is not None:
            node_to_add = list2.head
            new_l2_head = list2.head.next
            # print(current_node)
            # if self.head.node_value() > list2.head.node_value():
            if list2.head.node_value() <= current_node.node_value():

                list2.head = new_l2_head
                if current_node == self.head:
                    self.head = node_to_add
                    self.head.next = current_node
                else:
                    previous_node.next = node_to_add
                    node_to_add.next = current_node
                    current_node = node_to_add
                continue
            if current_node.next is None:
                current_node.next = node_to_add
                list2.head = None
                # list2.head.next = None
                break

            previous_node = current_node
            current_node = current_node.next

        return self

## Solution accepted by Leet:
# def mergeTwoLists(l1, l2):
#     merged = Node()
#     temp = merged
#     current_l1 = l1.head
#     current_l2 = l2.head
#     print(current_l1)
#     while l1 and l2 :
#         if current_l1.node_value() < current_l2.node_value():
#             temp.next = current_l1
#             current_l1 = current_l1.next
#         else:
#             temp.next = current_l2
#             current_l2 = current_l2.next

#         temp = temp.next

#     if current_l1 is not None:
#         temp.next = current_l1
#     elif current_l2 is not None:
#         temp.next = current_l2

#     return merged.next 

if __name__ == '__main__':
    list1 = [1,2,4]
    # list1 = []
    # list1 = []
    list2 = [1,3,4]
    # list2 = []
    # list2 = [0]

    ll = LinkedList(list1)
    ll2 = LinkedList(list2)
    # arr = [1,3,4]
    # print(ll.head)
    # print(ll.get_length())
    # ll.add_node(3, 5)
    # print(ll)
    # print(ll2)
    # ll.combine_sorted_lists(ll2)
    # print(ll.nodes_array())
    print(ll.mergeTwoLists(ll2))
    pass

## Assumption: You're being passed an array on Node objects! So just link the nodes
# together!
# def solution(list1, list2):
#     if len(list1) == 0 and len(list2) == 0:
#         return []
    
#     elif len(list2) == 0:
#         return list1
    
#     elif len(list1) == 0:
#         return list2
    
#     new_list = []
#     current_node = list1[0]
#     previous_node = None
#     i = 0
#     while len(list2) != 0:

#         if list2[0].data <= list1[i].data:
#             item = list2.pop(0)
#             if i == 0:
#                 item.next = list1[i]
#                 list1.insert(0,item)
#             else:
#                 previous_node.next = item
#                 item.next = current_node
#                 list1.insert(i, item)
#                 current_node = list1[i]
#             continue

#         if i == len(list1)-1:
#             item = list2.pop(0)
#             list1[-1].next = item
#             list1.append(item)

#         previous_node = list1[i]
#         i += 1
#         current_node = list1[i]

#     return list1


# if __name__ == '__main__':
#     # list1 = [Node(1), Node(2), Node(4)]
#     # list2 = [Node(1), Node(3), Node(4)]
#     # list1 = []
#     # list2 = []
#     list1 = []
#     list2 = [Node(0)]
#     print(solution(list1, list2))

