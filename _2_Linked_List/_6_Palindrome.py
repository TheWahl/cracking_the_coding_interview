# Jacob Wahl
# 3/2/21
#
# Problem 2.6 - Implement a function to check if a linked list is a
#               palindrome.
#

from Linked_List import Linked_List, Node


def is_palindrome_helper(llist: Linked_List):

    fowards, backwards = is_palindrome(llist.head, '', '')

    print(fowards, backwards)

    return True if fowards.replace(' ', '') == backwards.replace(' ', '') else False


def is_palindrome(node: Node, fowards: str, backwards: str) -> tuple:
    if node == None:
        return fowards, backwards
    else:
        fowards += node.val
        fowards, backwards = is_palindrome(node.next, fowards, backwards)
        backwards += node.val
        return fowards, backwards


def string_to_list(li: list) -> list:
    ret_list = []
    for i in li:
        llist = Linked_List()
        for cur in i:
            llist.append(cur)
        ret_list.append(llist)

    return ret_list


test_cases = ['',
              'a',
              'aba',
              'abcba',
              'acda',
              'taco cat']
test_cases = string_to_list(test_cases)
print(test_cases)

test_cases = string_to_list(test_cases)

for i in test_cases:
    print(is_palindrome_helper(i))
