# Jacob Wahl
# 2/16/20
#
# Problem 2.2 - Implement an algorithm to find the kth to last element of a singly linked list.
#

from Linked_List import Linked_List
from random import randint


def kth_to_last(list: Linked_List, k: int) -> Linked_List:
    # k = 1 means retreive the last elements
    # k = 2 means retreive the 2nd to last element

    if k > len(list):
        raise IndexError('k exceeds length of linked list')

    traverse_amount = len(list) - k

    # return list.get(traverse_amount)

    cur = list.head
    while traverse_amount > 0:
        cur = cur.next
        traverse_amount -= 1

    return cur.val


test_case = Linked_List()
length = 10
for i in range(length):
    test_case.append(randint(1, 50))

print(test_case)
for i in range(1, length+1):
    print(kth_to_last(test_case, i))
