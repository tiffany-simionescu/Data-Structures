"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def __str__(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            output += f"{current_node.value}"
            # Update the tracker node to the next node
            current_node = current_node.next_node
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
          new_node.next_node = self.head 
          self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def get_list_size(self):
        i = 0
        current_item = self.head
        if not current_item:
            return i
        while current_item is not None:
            i += 1
            current_count = i
            current_item = current_item.next_node
        return current_count

### Original class Stack - using an Array ###
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         size_length = len(self.storage)
#         self.size = size_length
#         return size_length

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()


### Class Stack - Linked List ###

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        return None
