# Huffman Coding

"""
Phase 1 - Build the Huffman Tree
Determine frequency of each (unique) character
Make node(character, frequency, left_child, right_child)
Repeat: pop node with lowest frequency
Build and sort list of nodes from low to high frequency
Priority queue (lower freq = higher priority)
Pop two min. freq. nodes from queue
Create new node with frequency = sum(two popped nodes) [internal node]
New node in Huffman tree with popped nodes as children

Repeat [implement min-heap tree]

Then assign 0 to left child and 1 to right child

"""

import time, copy, sys, heapq
from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Node(object):
    def __init__(self, character, value):
        self.character = character
        self.value = value
        self.left = None
        self.right = None
        self.bit = None

    def __repr__(self):
        s = "[{}:{}]".format(self.character, self.value)

        return s


def bfs(root):
    """
    Breadth-first search for binary trees. Returns a visit order list. (Method used for debugging)

    :param root: root of binary tree
    :return: list (visit order)
    """
    visit_order = list()
    q = Queue()
    # print("bfs root:{}".format(root))
    q.enq(root)  # enqueue root

    def traverse(node):  # define recursion and exit condition
        if node:
            # print("traverse node:{}".format(node))
            visit_order.append(node)  # visit node
            # print("has left?:{} has right?{}".format(node.left, node.right))
            if node.left:  # enqueue children (left then right)
                # print("left node:{}".format(node.left))
                q.enq(node.left)
            if node.right:
                # print("right node:{}".format(node.right))
                q.enq(node.right)
            # print(f"visit order: {visit_order}")
            traverse(q.deq())  # traverse left/right children recursively

    traverse(q.deq())
    # print(visit_order)
    return visit_order


class MinHeapTree(object):  # attempted to create heapq before knowing it existed
    """
    Stores nodes such that the parent node is less than or equal to its children.

    Attributes
    ----------
    root : Node
        A Node object.

    Methods
    -------
    compare(node_1, node_2):
        Compares two nodes and returns and integer representing their value relationship.
    insert(new_node):
        Inserts a new Node into MinHeapTree.
    remove(target):
        Remove node from MinHeapTree.
    swap(target, q):
        Swaps target with smallest child until the base (search order stored in q [Queue]). Returns a visit order list.
    pop():
        Returns and removes root (lowest value) and rearranges tree.

    """

    def __init__(self, node=None):
        self.root = node
        # self.visit_order = list()

    def compare(self, node_1, node_2):
        """
        Compares two nodes and returns and integer representing their value relationship.
        :param node_1: Node
        :param node_2: Node
        :return: 0 if nodes are equal, -1 if node_2 is less than node_1, 1 if node_2 is greater than node_1
        """
        # print("COMPARE CALLED")

        if node_2.value == node_1.value:
            return 0
        elif node_2.value < node_1.value:
            return -1
        else:
            return 1

    def insert(self, new_node):
        """
        Inserts a node into MinHeapTree.

        :param new_node: Node
        :return: None
        """

        # print("INSERT CALLED")
        print("new node{}".format(new_node))

        if not self.root:  # Empty tree
            self.root = new_node
            # print(
            #     "[{}:{}]({}|{}|{})".format(new_node.character, new_node.value, new_node.left,
            #                                new_node.parent, new_node.right))
            return

        # def print_node(node):  # debugging
        #     print(
        #         "[{}:{}]({}|{}|{})".format(node.character, node.value, node.left,
        #                                    node.parent, node.right))
        def fill_empty(old_node, node):
            """
            Fills empty leaves with node.
            :param old_node: Node
            :param node: Node
            :return:
            """
            if not old_node.left:  # left is empty
                old_node.left = node
                old_node.left.parent = old_node
                return
            else:  # left not empty, check if right is empty
                if not old_node.right:  # right is empty
                    old_node.right = node
                    old_node.right.parent = old_node
                    return

        def traverse_insert(node):  # bfs search
            """
            Performs a breadth first search on tree and inserts node.
            :param node: Node
            :return:
            """
            q = Queue()

            if node:
                print("traversing node:{}".format(node))
                # time.sleep(2)
                # visit_order.append(node)  # visit node

                decision = self.compare(node, new_node)
            if decision == 0:  # new_node value == node value
                print("{}=={}".format(new_node, node))
                fill_empty(node, new_node)
                if self.compare(node.left, new_node) == -1 or self.compare(node.right,
                                                                           new_node) == -1:  # new_node smaller than parent
                    if self.compare(node.left, node.right) == -1:
                        pass
                    elif self.compare(node.left, node.right) == 1:
                        pass



            elif decision == -1:  # new_node value < node value
                print("{}<{}".format(new_node, node))
                # print(self.swap(new_node))
                if node is self.root:  # update root
                    self.root = new_node
                else:
                    if node.parent.left is node:  # update parent if node is not root
                        node.parent.left = new_node
                    elif node.parent.right is node:
                        node.parent.right = new_node

                new_node.parent = node.parent  # update new_node parent
                new_node.right = node.right  # attach node right to new_node right
                node.parent = new_node  # update node parent
                node.right = None  # detach node right
                new_node.left = node  # attach node to new_node left

                if node.right:  # if not None
                    new_node.right.parent = new_node  # update right parent
                # print(
                #     "[{}:{}]({}|{}|{})".format(new_node.character, new_node.value, new_node.left,
                #                                new_node.parent, new_node.right))
                return
            else:  #
                pass

            if node.left:  # enqueue children (left then right)
                q.enq(node.left)
            if node.right:
                q.enq(node.right)

            print("TRAVERSE")
            traverse_insert(q.deq(), new_node)  # traverse left/right children recursively

        traverse_insert(self.root)

        return

    def remove(self, target):
        """
        Remove node from MinHeapTree.
        :param target: Node (to be removed)
        :return: None
        """

        # print("REMOVE CALLED")
        q = Queue()
        q.enq(self.root)  # enqueue root

        def traverse(node):  # define recursion and exit condition
            if node:
                if target is node:
                    # print("target{} parent is {}".format(target, target.parent))
                    if target is self.root:
                        self.root = None  # remove tree root
                        return
                    if target.parent.left is node:  # remove node
                        target.parent.left = None
                    else:
                        target.parent.right = None
                    target.parent, target.left, target.right = None, None, None
                    return
                if node.left:  # enqueue children (left then right)
                    q.enq(node.left)
                if node.right:
                    q.enq(node.right)
                traverse(q.deq())  # traverse left/right children recursively

        traverse(q.deq())
        return

    def swap(self, target):
        """
        Swaps target with smallest child below target. Returns a visit order list.
        :param target: Node
        :return: list (visit_order)
        """

        # print("SWAP CALLED")

        q = Queue()
        visit_order = list()

        if target:
            # print("target node:{}".format(target))
            visit_order.append(target)  # visit node
            if target.left is None and target.right is None:
                return  # end of branch
            elif target.right is None and target.left:
                compare_children = 1
            elif target.left is None and target.right:
                compare_children = -1
            else:
                compare_children = self.compare(target.left, target.right)
            parent = target  # renamed for clarity
            parent_parent, parent_left, parent_right = parent.parent, parent.left, parent.right
            if compare_children in [0, 1]:  # left smaller or equal to right
                # print("{} smaller(left) than or equal to {}".format(target.left, target.right))
                # time.sleep(2)
                if self.compare(target.left, target) == 1:  # left is smaller than parent
                    # print("{}(left child) smaller than {})".format(target.left, target))
                    swap_node = target.left
                    # update parent
                    # print(
                    #     "Original parent{}({}|{}|{})".format(parent, parent.left, parent.parent, parent.right))
                    # print("Original child{}({}|{}|{})".format(swap_node, swap_node.left, swap_node.parent,
                    #                                           swap_node.right))
                    if parent.right:
                        parent.right.parent = swap_node
                    if parent.parent:
                        if parent.parent.left is parent:
                            parent.parent.left = swap_node
                        elif parent.parent.right is parent:
                            parent.parent.right = swap_node
                    parent.parent, parent.left, parent.right = swap_node, swap_node.left, swap_node.right
                    # print(
                    #     "New parent{}({}|{}|{})".format(parent, parent.left, parent.parent, parent.right))
                    # update swap_node
                    if target is self.root:
                        self.root = swap_node
                    if swap_node.left:
                        swap_node.left.parent = parent
                    elif swap_node.right:
                        swap_node.right.parent = parent
                    swap_node.parent, swap_node.left, swap_node.right = parent_parent, parent, parent_right
                    # print("New child{}({}|{}|{})".format(swap_node, swap_node.left, swap_node.parent,
                    #                                      swap_node.right))
                    q.enq(parent)  # keep swapping down tree
                else:  # left is greater than or equal to parent
                    return visit_order

            elif compare_children == -1:  # right smaller than left
                # print("{} smaller(right) than {}".format(target.right, target.left))
                # time.sleep(2)
                if self.compare(target.right, target) == 1:  # right is smaller than parent
                    # print("{}(right child) smaller than {}(parent)".format(target.right, target))
                    swap_node = target.right
                    # update parent
                    if parent.left:
                        parent.left.parent = swap_node
                    if parent.parent:
                        if parent.parent.left is parent:
                            parent.parent.left = swap_node
                        elif parent.parent.right is parent:
                            parent.parent.right = swap_node
                    parent.parent, parent.left, parent.right = swap_node, swap_node.left, swap_node.right
                    # update swap_node
                    if target is self.root:
                        self.root = swap_node
                    if swap_node.left:
                        swap_node.left.parent = parent
                    elif swap_node.right:
                        swap_node.right.parent = parent
                    swap_node.parent, swap_node.left, swap_node.right = parent_parent, parent_left, parent
                    q.enq(parent)  # keep swapping down tree
            # print("ROOT{}({}|{}|{})".format(self.root, self.root.left, self.root.parent,
            #                                      self.root.right))
            # print(tree)
            self.swap(target)  # traverse

        return visit_order

    def pop(self):
        """
        Returns and removes root (lowest value) and rearranges tree.
        :return: Node (lowest value in heap)
        """

        print("POP CALLED")
        node_pop = self.root
        visit_order = list()
        q = Queue()
        if node_pop is None:
            return "No elements in tree."
        if node_pop.left or node_pop.right:  # more than one tree element
            q.enq(node_pop)  # enqueue root

            def traverse_pop(node):  # define recursion and exit condition
                if node:
                    print("traverse node:{}".format(node))
                    visit_order.append(node)  # visit node
                    # print("has left?:{} has right?{}".format(node.left, node.right))
                    if node.left:  # enqueue children (left then right)
                        # print("left node:{}".format(node.left))
                        q.enq(node.left)
                    if node.right:
                        # print("right node:{}".format(node.right))
                        q.enq(node.right)
                    # print(f"visit order: {visit_order}")
                    traverse_pop(q.deq())  # traverse left/right children recursively

            traverse_pop(q.deq())
            node_sort = visit_order[-1]  # move lowest element in tree to root and swap down (sort node)
            self.remove(node_sort)  # remove sorting node from tree (prevent duplicate)
            # update root
            node_sort.parent, node_sort.left, node_sort.right = None, self.root.left, self.root.right
            if self.root.left:
                self.root.left.parent = node_sort
            elif self.root.right:
                self.root.right.parent = node_sort
            self.root = node_sort
            self.swap(self.root)  # sort tree with sorting node
        else:
            self.remove(node_pop)  # single element tree, ensures tree destruction

        node_pop.parent, node_pop.left, node_pop.right = None, None, None  # reset node_pop pointers

        return node_pop

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.root
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()

            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.left:
                q.enq((node.left, level + 1))
            else:
                q.enq((None, level + 1))

            if node.right:
                q.enq((node.right, level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s  #


class HuffmanNode(object):
    """
    A class to represent a Huffman encoding node.

    Attributes
    ----------
    value : int
        Sum of children values.
    left : tuple (frequency, character) or HuffmanNode
        A HuffmanNode or Node object.
    right : tuple (frequency, character) or HuffmanNode
        A HuffmanNode or Node object.

    """

    def __init__(self, left, right):

        self.left = left
        self.right = right

        if type(left) == tuple:  # convert to Node
            self.left = Node(left[1], left[0])
        if type(right) == tuple:
            self.right = Node(right[1], right[0])

        self.left.bit = 0
        if right:
            self.right.bit = 1
            self.value = self.left.value + self.right.value
        else:  # single character case
            self.value = self.left.value
        self.bit = None

    def __str__(self):
        s = "[{}]".format(self.value)

        return s


class HuffmanTree(object):
    """
    Stores HuffmanNode and Nodes such that each parent is the sum of its children's value. Bits are assigned to node children, left is 0, right is 1.
    """

    def __init__(self, node=None):
        self.root = node
        self.count = 0

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.root
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.left:
                q.enq((node.left, level + 1))
            else:
                q.enq((None, level + 1))

            if node.right:
                q.enq((node.right, level + 1))
            else:
                q.enq((None, level + 1))
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s


def huffman_encoding(data):
    """
    Huffman encodes data.
    :param data: string (to encode)
    :return: string (data as Huffman encoded string)
    """

    print('String to encode: [{}]'.format(data))
    char_bins = {}  # to store character and frequency counts
    heap = []  # new heap
    hufftree = HuffmanTree()
    code = {}  # to store Huffman codes
    output = ""  # the Huffman encoded string

    # Build the Huffman Tree
    for char in data:
        if char in char_bins.keys():
            char_bins.update({char: char_bins.get(char) + 1})  # store data as a dict by character and count
        else:
            char_bins[char] = 1  # character not in dictionary

    for char, freq in char_bins.items():  # build heap
        heapq.heappush(heap, (freq, char))
    # print(heap)

    def grow(leaves, tree, count):
        """
        Populates and returns a HuffmanTree.
        :param leaves: heap
        :param tree: HuffmanTree
        :param count: int (number of HuffmanNodes in HuffmanTree)
        :return: HuffmanTree
        """
        if count == 0:  # empty tree
            if len(leaves) == 0:  # No data to encode
                return None
            elif len(leaves) == 1:  # One character to encode
                tree.root = HuffmanNode(heapq.heappop(leaves), None)
                return tree
            else:  # populate root
                tree.root = HuffmanNode(heapq.heappop(leaves), heapq.heappop(leaves))
                count += 1
        else:
            if len(leaves) == 2:  # this ensures the last two Nodes go to the right of a populated tree root
                right = HuffmanNode(heapq.heappop(leaves), heapq.heappop(leaves))
                tree.root = HuffmanNode(tree.root, right)
                return tree
            else:  # build tree
                tree.root = HuffmanNode(tree.root, heapq.heappop(leaves))
                count += 1
        grow(leaves, tree, count)

        return tree

    hufftree = grow(heap, hufftree, 0)
    # print(hufftree)

    if hufftree is None:  # no characters to encode
        print("No data to encode.")
        return None, None

    # Generate the Encoded Data
    # traverse tree to build encoding dictionary
    def in_order(root, level, code_bins):
        if type(root) == HuffmanNode:
            if not root.right:  # single character case
                code_bins[root.left.character] = str(root.left.bit)
                return code_bins
            else:
                level += 1
                in_order(root.left, level, code_bins)
                if type(root.left) == Node:
                    code_bins[root.left.character] = str(root.left.bit) * level
                if type(root.right) == Node:
                    code_bins[root.right.character] = (str(root.left.bit) * (level - 1)) + str(root.right.bit)
                else:
                    code_bins[root.right.left.character] = (str(root.right.bit) * level) + str(root.left.bit)
                    code_bins[root.right.right.character] = (str(root.right.bit) * level) + str(root.right.bit)
        return code_bins

    if hufftree.root is None:
        output = ""
    else:
        code = in_order(hufftree.root, 0, code)
        # print(code)
        for char in data:
            output += str(code[char])
    return output, hufftree  # returns encoded string and Huffman Tree


def huffman_decoding(data, tree):
    """
    Decodes Huffman encoded data.
    :param data: string (Huffman encoded bits)
    :param tree: HuffmanTree
    :return: string (decoded Huffman data as output)
    """
    output = ""
    data = list(data)

    def traverse_decode(root, code):
        bit = code.pop(0)
        # print("root:{} bit:{}".format(root, int(bit)))
        if int(bit) == 0:
            # print("GO LEFT")
            if type(root.left) is Node:
                # print("DECODED:{}".format(root.left.character))
                return root.left.character
            else:  # go to lower level
                # print("to:{}".format(root.left))
                return traverse_decode(root.left, code)
        else:
            # print("GO RIGHT")
            if type(root.right) is Node:
                # print("DECODED:{}".format(root.right.character))
                return root.right.character
            else:  # Huffman node holding two highest frequency characters
                # print("to:{}".format(root.right))
                return traverse_decode(root.right, code)

    while len(data) > 0:  # decode the bit list
        output += traverse_decode(tree.root, data)
    return output


if __name__ == "__main__":
    codes = {}
    tests = ["The bird is the word",
             "AAAAAAAA",
             "The quick brown fox jumps over the lazy dog",
             "Cozy sphinx waves quart jug of bad milk"]
    # a_great_sentence = "The bird is the word"
    for a_great_sentence in tests:
        print(a_great_sentence)
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

# Test cases

# # test = "The bird is the word"
# test = "Kaito Degnan is a happy slappy pappy"
# # data = 'AAAAAAAAAA'
# # data = ''
# # test = '1111111111111100100100110101010101010000000010101010101'
# encoded, ki = huffman_encoding(test)
# print(encoded)
# print(huffman_decoding(encoded, ki))

