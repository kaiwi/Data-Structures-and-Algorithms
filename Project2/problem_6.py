# Union and Intersection of Two Linked Lists

#        Union: set of elements which are in A, in B, or in both A and B.
# Intersection: set of all objects that are members of both the sets A and B.

# Take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
# Once you have completed the problem you will create your own test cases and perform your own run time analysis on the
# code.
from time import sleep

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_set(self):
        """
        Returns a list of this object's elements.
        :return: A list containing this object's elements.
        """
        output = set()
        node = self.head
        while node:
            output.add(node.value)
            node = node.next

        return output


def union(llist_1, llist_2):
    """
    Returns a LinkedList containing all elements from both arguments.
    :param llist_1: A LinkedList.
    :param llist_2: A LinkedList.
    :return: A LinkedList containing the union of the arguments.
    """
    head_list = [llist_1.head, llist_2.head]
    llist_union = LinkedList()
    for head in head_list:  # iterate through LinkedList heads
        node = head
        while node is not None:  # iterate through each LinkedList
            llist_union.append(node.value)  # add a new node to union LinkedList; O(n*m)
            node = node.next

    return llist_union


def intersection(llist_1, llist_2):
    """
    Returns a LinkedList containing elements common to both LinkedList arguments.
    :param llist_1: A LinkedList.
    :param llist_2: A LinkedList.
    :return: A LinkedList containing the intersection of the arguments.
    """
    llist_intersection = LinkedList()
    set_1, set_2 = llist_1.to_set(), llist_2.to_set()
    while len(set_1.intersection(set_2)) > 0:  # intersection set; O(min(len(m), len(n)))
        llist_intersection.append(set_intersection.pop())  # pop elements off set and convert to a LinkedList

    return llist_intersection


if __name__ == "__main__":
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("UNION:{}".format(union(linked_list_1, linked_list_2)))
    print("INTERSECTION: {}".format(intersection(linked_list_1, linked_list_2)))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("UNION:{}".format(union(linked_list_3, linked_list_4)))
    print("INTERSECTION: {}".format(intersection(linked_list_3, linked_list_4)))

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [1, 1, 1, 1]
    element_2 = [1, 1, 1, 1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print("UNION:{}".format(union(linked_list_5, linked_list_6)))
    print("INTERSECTION: {}".format(intersection(linked_list_5, linked_list_6)))
