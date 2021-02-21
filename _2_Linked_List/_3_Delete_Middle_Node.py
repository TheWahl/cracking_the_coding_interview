# Jacob Wahl
# 2/16/21
#
# Problem 2.3 - Implement an algorithm to delete a node in the middle (i.e. any node that's not the firtst or last) of a singly linked list, given only access to that node.
#

from Linked_List import Linked_List, Node
from random import randint


def remove_node(node: Node):
    # Since given node is in the middle of the list,
    # we can copy contents of node.next into node and then skip node.next

    node.val = node.next.val
    node.next = node.next.next


test_case = Linked_List()
for i in range(4):
    test_case.append(randint(0, 9))
print(test_case)
remove_node(test_case.get(2, True))
print(test_case)
