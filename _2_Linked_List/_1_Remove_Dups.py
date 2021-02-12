# Jacob Wahl
# <Date>
#
# Problem 2.1 - Write code to remove duplicates from an unsorted linked list.
#               FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

from Linked_List import LinkedList


def removeDuplicates(list: LinkedList) -> LinkedList:

    if len(list) <= 1:  # List is comprised of 1 or 0 elements
        return list

    cur = list.head
    while cur.next != None:

    return list


test_case = LinkedList()
for i in [2, 2, 2]:
    test_case.append(i)

print(removeDuplicates(test_case))
