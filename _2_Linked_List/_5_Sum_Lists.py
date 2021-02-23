# Jacob Wahl
# 2/20/20
#
# Problem 2.5 - You have two numbers represented by a linked list, where each
#               node contains a single digit. The digits are stored in reverse
#               order, such that the 1's digit is at the head of the list.
#               Write a function that adds the two numbers and returrns the
#               sum as a linked list.
#               FOLLOW UP: Suppose the digits are stored in foward order.
#                          Repeat the above problem.

from random import randint
from Linked_List import Linked_List


def sum_lists(a: Linked_List, b: Linked_List) -> Linked_List:

    a_runner = a.head
    b_runner = b.head
    new = Linked_List()
    remainder = 0
    while (a_runner != None or b_runner != None):

        if b_runner == None:
            tot_sum = a_runner.val + remainder
            remainder = tot_sum // 10
            val = tot_sum - (remainder * 10)

            new.append(val)

            a_runner = a_runner.next

        elif a_runner == None:
            tot_sum = b_runner.val + remainder
            remainder = tot_sum // 10
            val = tot_sum - (remainder * 10)

            new.append(val)

            b_runner = b_runner.next

        else:
            tot_sum = a_runner.val + b_runner.val + remainder
            remainder = tot_sum // 10
            val = tot_sum - (remainder * 10)

            new.append(val)

            a_runner = a_runner.next
            b_runner = b_runner.next

    if remainder > 0:
        new.append(remainder)

    return new


def sum_lists_follow_up(a: Linked_List, b: Linked_List):

    new_stack = []
    stack_a = []
    stack_b = []
    remainder = 0

    cur = a.head
    while cur != None:
        stack_a.append(cur.val)
        cur = cur.next

    cur = b.head
    while cur != None:
        stack_b.append(cur.val)
        cur = cur.next

    while stack_a or stack_b:
        if stack_a and stack_b:
            val_a = stack_a.pop()
            val_b = stack_b.pop()

            tot_sum = val_a + val_b + remainder
            remainder = tot_sum // 10
            val = tot_sum - (remainder * 10)

            new_stack.append(val)
        elif stack_b:
            val_b = stack_b.pop()

            tot_sum = val_b + remainder
            remainder = tot_sum // 10
            val = tot_sum - (remainder * 10)

            new_stack.append(val)
        else:
            val_a = stack_a.pop()

            tot_sum = val_a + remainder
            remainder = tot_sum // 10
            val = tot_sum - (remainder * 10)

            new_stack.append(val)

    if remainder > 0:
        new_stack.append(remainder)

    new = Linked_List()
    while new_stack:
        new.append(new_stack.pop())

    return new


test_case_a = Linked_List()
test_case_b = Linked_List()
length_a = 3
length_b = 3
for i in range(length_a):
    test_case_a.append(randint(0, 9))
for i in range(length_b):
    test_case_b.append(randint(0, 9))
print(test_case_a)
print(test_case_b)
print()
print(sum_lists(test_case_a, test_case_b))
