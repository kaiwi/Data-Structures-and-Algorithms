# Huffman Coding

import sys
import heapq
from collections import deque


class Queue():
    """
    Class objects model a simple queue.
    """
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
    """
    Class objects represent a single character and frequency value of a string. Objects stores a bit to be used during
    Huffman encoding/decoding.
    """
    def __init__(self, character, value):
        """
        Constructor for Node.
        :param character: String of length 1.
        :param value: Integer
        """
        self.character = character
        self.value = value
        self.bit = None

    def __repr__(self):
        s = "[{}:{}]".format(self.character, self.value)

        return s


class HuffmanNode(object):
    """
    A class to represent a Huffman encoding node.
    """

    def __init__(self, left, right):
        """
        Constructor for HuffmanNode
        :param left: A tuple (frequency, character) or HuffmanNode.
        :param right:  A tuple (frequency, character) of HuffmanNode.
        """
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
    A class to stores HuffmanNode and Nodes such that each parent is the sum of its children's value. Bits are
    assigned to node children, left is 0, right is 1.

    Attributes
    ----------
    root : HuffmanNode
        A HuffmanNode.
    count : int
        Integer to count bit depth for encoding/decoding.
    """

    def __init__(self, node=None):
        """
        Constructor for HuffmanTree.
        :param node: A HuffmanNode.
        """
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
    :return: A Huffman encoded string (of data) and the HuffmanTree used for encoding.
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

    if hufftree is None:  # no characters to encode
        print("No data to encode.")
        return None, None

    # Generate the Encoded Data
    # traverse tree to build encoding dictionary
    def in_order(root, level, code_bins):
        """
        Performs an in-order binary tree search on the HuffmanTree to produce the final encoded output.
        :param root: A HuffmanNode.
        :param level: Integer to track recursion depth to be used to generate individual character bit codes.
        :param code_bins: A dictionary for individual character bit codes.
        :return: A dictionary containing all individual character bit codes.
        """
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
    if data is None:
        print("Nothing to decode.")
        output = data
    else:
        output = ""
        data = deque(list(data))

        def traverse_decode(root, code):
            bit = code.popleft()
            if int(bit) == 0:
                if type(root.left) is Node:
                    return root.left.character
                else:  # go to lower level
                    return traverse_decode(root.left, code)
            else:
                if type(root.right) is Node:
                    return root.right.character
                else:  # Huffman node holding two highest frequency characters
                    return traverse_decode(root.right, code)

        while len(data) > 0 and tree.root:  # decode the bit list
            output += traverse_decode(tree.root, data)
    return output


if __name__ == "__main__":
    codes = {}
    tests = ["The bird is the word",
             "AAAAAAAA",
             "The quick brown fox jumps over the lazy dog",
             "Cozy sphinx waves quart jug of bad milk",
             ""]
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


