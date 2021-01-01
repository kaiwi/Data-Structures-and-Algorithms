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

    def __lt__(self, other):
        return other < self.value

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

    def __lt__(self, other):
        return other < self.value

    def __repr__(self):
        s = "[{}]".format(self.value)

        return s


def view_heap(heap):
    """
    To visualize heaps.
    :param heap: a heap of Nodes and HuffmanNodes.
    :return: String representation of heap as a binary tree.
    """
    level = 0
    q = Queue()
    visit_order = list()
    node = heap[0]
    q.enq((node, level))
    while len(q) > 0:
        node, level = q.deq()
        if node is None:
            visit_order.append(("<empty>", level))
            continue
        visit_order.append((node, level))
        if type(node) != Node and node.left:
            q.enq((node.left, level + 1))
        else:
            q.enq((None, level + 1))

        if type(node) != Node and node.right:
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
    char_bins = {}  # to store character and frequency counts
    heap = []  # new heap
    code = {}  # to store Huffman codes
    output = ""  # the Huffman encoded string

    # Build the minheap
    for char in data:
        if char in char_bins.keys():
            char_bins.update({char: char_bins.get(char) + 1})  # store data as a dict by character and count
        else:
            char_bins[char] = 1  # character not in dictionary

    for char, freq in char_bins.items():  # build heap
        heapq.heappush(heap, Node(char, freq))

    if len(heap) == 1:  # single character data string
        heapq.heappush(heap, HuffmanNode(heapq.heappop(heap), None))  # push HuffmanNode into heap
    else:
        while len(heap) > 1:
            heapq.heappush(heap, HuffmanNode(heapq.heappop(heap), heapq.heappop(heap)))  # push HuffmanNode into heap

    # Generate the Encoded Data
    # traverse tree to build encoding dictionary

    def in_order(root, code_bins, level=""):
        """
        Performs an in-order binary tree search on the HuffmanTree to produce the final encoded output.
        :param root: A HuffmanNode.
        :param code_bins: A dictionary for individual character bit codes.
        :param level: String to track recursion depth to be used to generate individual character bit codes.
        :return: A dictionary containing all individual character bit codes.
        """

        if type(root) == HuffmanNode:
            if not root.right:  # single character case
                code_bins[root.left.character] = str(root.left.bit)
                return code_bins
            else:
                in_order(root.left, code_bins, level+"0")  # go left

                if type(root.left) == Node:
                    code_bins[root.left.character] = level + str(root.left.bit)
                if type(root.right) == Node:
                    code_bins[root.right.character] = level + str(root.right.bit)

                in_order(root.right, code_bins, level+"1")  # go right
        return code_bins

    if len(heap) == 0:  # nothing to encode
        output = ""
    else:
        code = in_order(heap[0], code)
        for char in data:
            output += str(code[char])
    return output, heap


def huffman_decoding(data, heap):
    """
    Decodes Huffman encoded data.
    :param data: string (Huffman encoded bits)
    :param heap: a heap of Nodes and HuffmanNodes
    :return: string (decoded Huffman data as output)
    """
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
            else:  # go to lower level
                return traverse_decode(root.right, code)

    while len(data) > 0:  # decode the bit list
        output += traverse_decode(heap[0], data)
    return output


if __name__ == "__main__":
    codes = {}
    tests = ["The bird is the word",
             "AAAAAAAA",
             "The quick brown fox jumps over the lazy dog",
             "Cozy sphinx waves quart jug of bad milk",
             "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"]
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
