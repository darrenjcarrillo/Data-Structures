"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.previous = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    # ADD TO HEAD
    def add_to_head(self, value):
        # create new_node
        new_node = ListNode(value)

        # 1. add to empty
        if self.head is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node

        # 2. add to if not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node
        # update increment length attribute
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    # REMOVE FROM HEAD

    def remove_from_head(self):
        # # store the value of the head
        # curretHead = self.head

        # # Delete the head
        # # if head is NOT empty
        # if self.head.next is not None:
        #     # set head.next's prev to self's None
        #     self.head.next.prev = None
        #     # set head to head.next
        #     self.head = curretHead.next
        # # Else if next head empty
        # else:
        #     # set head to None
        #     self.head = None
        #     # set tail to None
        #     self.tail = None
        # # decrement the length of the DLL
        # self.length -= 1
        # # return the value
        # return curretHead.value

        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    # ADD TO TAIL

    def add_to_tail(self, value):
        # create new_node
        new_node = ListNode(value)

        # add to empty
        if self.tail is None:
            # set head and tail to the new node instace
            self.head = new_node
            self.tail = new_node
        # add to if not empty
        else:
            # set new node's next to current tail
            new_node.prev = self.tail
            # set tail's prev to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node
        # update increment length attribute
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    # REMOVE FROM TAIL

    def remove_from_tail(self):
        # store the value of the tail
        currentTail = self.tail

        # Delete the tail
        # If tail is NOT empty
        if self.tail.prev is not None:
            # set tail.next's prev to self's None
            self.tail.prev = None
            # set tail to head.next
            self.tail = currentTail.prev
        # Else if next tail empty
        else:
            # set tail to None
            self.tail = None
            # set head to None
            self.head = None

        # decrement the length of the DDL
        self.length -= 1
        # return the value
        return currentTail.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    # MOVE TO FRONT

    def move_to_front(self, node):
        if node is self.head:
            return
        # 1. delete
        else:
            self.delete(node)
        # 2. add_to_head()
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    # MOVE TO END
    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            self.delete(node)
            self.add_to_tail(node.value)
    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    # DELETE

    def delete(self, node):
        # DO not need to update head, tail/return value
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:  # list has +2 nodes
            self.head = node.next
            # updating prev and/or next pointers
        elif node is self.tail:
            self.tail = node.prev
        # If it's somewhere else
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    # GET MAX

    def get_max(self):
        # start at the head
        current_val = self.head
        max_val = self.head.value
        # set the
        while current_val.next is not None:
            current_val = current_val.next
            if current_val.value > max_val:
                max_val = current_val.value
        return max_val
