class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

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
    # Lecture Version
    # def contains(self, value):
    #     cur_node = self.head
    #     while cur_node is not None:
    #         if value == cur_node.get_value():
    #             return True
    #         cur_node = cur_node.get_next()
    #     return False

    def get_max(self):
        if self.head is None:
            return None
        cur_max = self.head.get_value()
        cur_node = self.head.get_next()

        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max

    # Not in test but part of lecture
    def remove_tail(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()

            value = self.tail.get_value()
            cur_node.set_next(None)
            self.tail == cur_node
            return value