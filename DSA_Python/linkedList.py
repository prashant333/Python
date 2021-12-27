# Linked list data structure implementation in python

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


# Initializing the linked list

linked_list = LinkedList()

# here we are creating independent nodes

linked_list.head = Node("how")
second = Node("are")
third = Node("you")

# connecting the nodes
linked_list.head.next = second
second.next = third

# printing the linked list values
while linked_list.head is not None:
    print(linked_list.head.val, end=" ")
    linked_list.head = linked_list.head.next
