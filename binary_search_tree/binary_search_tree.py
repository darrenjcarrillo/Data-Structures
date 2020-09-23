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
        # one side then other
        # on every single node, call the fn(value)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
