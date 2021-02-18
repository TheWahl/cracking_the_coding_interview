# Jacob Wahl
# 2/16/20
#
# Problem 2.2 - Implement an algorithm to find the kth to last element of a singly linked list.
#

from Linked_List import Linked_List, Node
from random import randint


def kth_to_last(list: Linked_List, k: int, know_length=True) -> Node:
    # k = 1 means retreive the last elements
    # k = 2 means retreive the 2nd to last element

    if list.head == None:
        raise ValueError('list is empty')

    if k < 1:
        raise IndexError('k must be greater than or equal to 1')

    # If we know list length
    if know_length:
        if k > len(list):
            raise IndexError('k exceeds length of linked list')

        traverse_amount = len(list) - k

        # return list.get(traverse_amount)

        cur = list.head
        while traverse_amount > 0:
            cur = cur.next
            traverse_amount -= 1

        return cur

    # If we don't know list length
    else:
        # We can make two runners traverse the list and have them spaced k-1 elements apart.
        # Then once the first runner reaches the end of the list, the second runner will
        # be equal to the kth to last element.

        front = list.head
        while k > 1:
            if front.next != None:
                front = front.next
                k -= 1
            else:
                raise IndexError('k exceeds length of list')

        tail = list.head
        while front.next != None:
            front = front.next
            tail = tail.next

        return tail


def recursive_helper_kth_to_last(list: Linked_List, k: int) -> Node:
    node, numb = recursive_kth_to_last(list.head, k)
    return node


def recursive_kth_to_last(node: Node, k: int) -> (int, Node):

    if node == None:
        return None, k
    else:
        ret_node, k = recursive_kth_to_last(node.next, k)
        if k == 1:
            ret_node = node

        k = 0 if k == 0 else k - 1

        return ret_node, k


test_case = Linked_List()
length = 3
for i in range(length):
    test_case.append(randint(1, 100))

print(test_case)
for i in range(1, length+1):
    print(recursive_helper_kth_to_last(test_case, i).val)
