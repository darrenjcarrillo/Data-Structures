"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


##### QUEUE #####

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(self.size, value)
        self.size += 1

    def dequeue(self):
        if (self.size > 0):
            val = self.storage[0]
            del self.storage[0]
            self.size -= 1
            return val

##### STACK #####


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
        # Case 1 - Value is less than root/self.value
        # if value < root
        if value < self.value:
            # if left child is None
            if self.left is None:
                # add here... left child = BSTNode(value)
                self.left = BSTNode(value)
            else:
                self.left.insert(value)  # recursive call

        # Case 2 - Value is greater than root/self.value
        # if value >= root (dupes go to the right)
        if value >= self.value:
            # if right child is None
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)  # recursive call

        # ITERATIVE APPROACH
        # while not at bottom level of tree
        # while self.value is not None:
        #     # if value < root
        #     if value < self.value:
        #         # if left child is None
        #         if self.left is None:
        #             # add here
        #             self.left = BSTNode(value)
        #         # exit loop

        #     # if value >= root (dupes go to the right)
        #     if value >= self.value:
        #         # if right child is None
        #         if self.right is None:
        #             # add here
        #             self.right = BSTNode(value)
        #     # exit loop

    # CONTAINS
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1 - if self.value is target. return TRUE
        if self.value == target:
            return True
        # Case 2 - if self.value is greater than target
        if self.value > target:
            # if self.left is None - its not in the tree
            if self.left is None:
                return False
            else:
                return self.right.contains(target)
        # Case 3 - Otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # GET MAX
    # Return the maximum value found in the tree

    def get_max(self):
        # go right until you cannot anymore
        # return value at far right
        if self.right:
            return self.right.get_max()
        return self.value

    # FOR EACH
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # go left, call fn(value)
        # go right, call fn(value)
        # one side then other
        # on every single node, call the fn(value)
        fn(self.value)  # call fn on root node

        # if self.left is None and self.right is None:  # Not needed
        #     return

        # Recursive case - 1 or more children
        if self.right:  # if there is right
            self.right.for_each(fn)
        if self.left:  # if there is left
            self.left.for_each(fn)

    # Part 2 -----------------------

    # IN ORDER PRINT
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # RECURSIVE - place your print statement in between recursive
        # calls that explore left & right subtrees
        if self is None:
            return

        # check to move left
        if self.left is not None:
            self.left.in_order_print(self.left)

        # print value
        print(self.value)

        # check to move right
        if self.right is not None:
            self.right.in_order_print(self.right)

        # ITERATIVE - think about the order in which we are adding nodes
        # to the stack

    # BREADTH FIRST TRAVERSAL PRINT
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # FIFO - First In First Out
        # use a queue to form a line
        queue = Queue()
        # for the nodes to "fall in line"

        # start by placing the root in the queue
        queue.enqueue(node)

        # Iterate while length of queue is greater than 0
        while queue.__len__() > 0:
            val = queue.storage[0]
            if val.left is not None:
                # place current items left node in queue if not None
                queue.enqueue(val.left)
            if val.right is not None:
                # place current items right node in queue if not None
                queue.enqueue(val.right)
            # print item
            queue.dequeue()
            print(val.value)

    # DEPTH FIRST TRAVERSAL
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create a stack to keep track of nodes we are processing
        stack = Stack()
        # push `self` into stack
        if node is not None:
            stack.push(node)
        # while something still on the stack (not done processing all nodes)
        while stack.__len__() > 0:
            val = stack.storage[-1]
            stack.pop()
            if val.right is not None:
                stack.push(val.right)
            if val.left is not None:
                stack.push(val.left)
            print(val.value)
        # use existing `for_each()` as a reference for traversal logic
        # push when we START pop when a node is DONE
        # and don't forget to call `print()`
        # +

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
bst.dft_print(bst)

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
