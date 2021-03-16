# Jacob Wahl
# 3/8/21
#
# Problem 2.8 - Given a circular linked list, implement an algorithm that
#               returns the node at the beginning of the loop.
#

from Linked_List import Linked_List, Node
from random import randint


def find_loop(llist: Linked_List) -> Node:

    if llist.head == None or llist.head.next == None:
        return False

    # Using a set
    '''
    runner = llist.head
    visited = set()
    while runner != None:

        if runner in visited:
            return runner
        else:
            visited.add(runner)
            runner = runner.next

    return False
    '''

    # Detecting loop with 2 runners
    fast_runner = llist.head.next
    slow_runner = llist.head
    while fast_runner != None and slow_runner != None:

        if fast_runner == slow_runner:
            break

        slow_runner = slow_runner.next

        fast_runner = fast_runner.next
        if fast_runner == None:
            return False
        else:
            fast_runner = fast_runner.next
    else:
        return False

    # Finding the beginning of the loop
    fast_runner = llist.head
    slow_runner = slow_runner.next

    while fast_runner != slow_runner:
        fast_runner = fast_runner.next
        slow_runner = slow_runner.next

    return fast_runner


length = 5
results = []
for i in range(length):

    llist = Linked_List()

    for _ in range(length):
        llist.append(randint(1, 100))

    print(llist, llist.get(i))
    #print(f' {i+1}: {find_loop(llist)}')
    resultA = find_loop(llist)
    llist.append(llist.get(i, return_node=True))
    #print(f' {i+1}: {find_loop(llist)}\n')
    resultB = find_loop(llist)

    if resultA == False and resultB == llist.get(i):
        results.append(True)

if all(results):
    print("All tests pass")
