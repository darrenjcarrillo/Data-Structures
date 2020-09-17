# a class that represents the individual elements in our LL
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create a new Node
        new_node = Node(value)
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            # update its pointer
            new_node.set_next_node(self.head)
            # update head
            self.head = new_node

        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create new Node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is NOT empty
        else:
            # update next_node of out tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # empty list
        if not self.head:
            return None

        # list with 1 element
        if not self.head.get_next_node():
            cur_head = self.head
            self.head = None
            self.tail = None
            return cur_head.get_value()

        # list with +2 elements
        val = self.head.get_value()
        self.head = self.head.get_next_node()
        return val

    def remove_tail(self):
        # empty list
        if not self.head:
            return None

        # list with 1 element
        if self.head is self.tail:
            ret_value = self.head.get_value()
            self.head = None
            self.tail = None
            return ret_value

        # list with +2 elements
        current_val = self.head

        while current_val.get_next_node() is not self.tail:
            current_val = current_val.get_next_node()

        value = self.tail.get_value()
        self.tail = current_val
        self.tail.set_next_node(None)
        return value

    def contains(self, value):
        # loop through LL until the next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find "value"
            if cur_node.get_value() == value:
                # return True
                return True
        return False

    def get_max(self):
        if self.head is None:
            return None
        max_val = self.head.get_value()
        current_val = self.head.get_next_node()

        while current_val:
            if current_val.get_value() > max_val:
                max_val = current_val.get_value()
            current_val = current_val.get_next_node()
        return max_val
