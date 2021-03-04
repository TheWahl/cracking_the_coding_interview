# Jacob Wahl
# 3/3/21
#
# Problem 2.7 - Given two singly linked lists, determine if the two lists
#               intersect. Return the intersecting node. Note that the
#               intersection is defined based on reference, not value. That
#               is, if the kth node of the first linked list is the exact same
#               node (by reference) as the jth node of the second linked list,
#               then they are intersecting.
#

from Linked_List import Linked_List, Node


def find_intersection(llist1: Linked_List, llist2: Linked_List) -> Node:

    # Determine lengths of lists
    length1 = 0
    cur = llist1.head
    while cur != None:
        length1 += 1
        cur = cur.next

    length2 = 0
    cur = llist2.head
    while cur != None:
        length2 += 1
        cur = cur.next

    runner1 = llist1.head
    runner2 = llist2.head

    # Moving pointers to
    if length2 > length1:
        diff = length2 - length1
        while diff > 0:
            runner2 = runner2.next
            diff -= 1

    elif length2 < length1:
        diff = length1 - length2
        while diff > 0:
            runner1 = runner1.next
            diff -= 1

    while runner1 != None and runner2 != None:
        if runner1 == runner2:
            return runner1
        else:
            runner1 = runner1.next
            runner2 = runner2.next

    return False


list1 = Linked_List()
list2 = Linked_List()
for i in [2, 3, 4]:
    list1.append(i)
for i in [5, 2, 7]:
    list2.append(i)

n = Node(99)
list1.append(n)
list2.append(n)
list1.append(12)
list1.append(52)

print(f'{list1}    {list2}')
print(find_intersection(list1, list2))
