# Jacob Wahl
# 2/19/21
#
# Problem 2.4 - Write code to partition a linked list around a value x, such
#               that all nodes less than x come before all nodes greater than
#               or equal to x. If x is contained within the list, the values
#               of x only need to be after the elements less than x. The
#               partiiton element x can appear anywhere in the 'right
#               partition'; it does not need to appear between the left and
#               right paritions.
#

from Linked_List import Linked_List
from random import randint
from collections import Counter


def partition(list: Linked_List, x: int) -> Linked_List:

    if 0 <= len(list) <= 1:
        return list

    # Apprach 1
    less = Linked_List()
    ge = Linked_List()

    cur = list.head
    while (cur != None):
        if cur.val < x:
            less.append(cur.val)
        else:
            ge.append(cur.val)

        cur = cur.next

    if less.isEmpty():
        return ge
    elif ge.isEmpty():
        return less
    else:
        less.get(len(less)-1, True).next = ge.head

    return less


test_case = Linked_List()
length = 3
for i in range(length):
    test_case.append(randint(0, 9))
print(test_case)
new = partition(test_case, 7)
print(new)
print(Counter(test_case) == Counter(new))
