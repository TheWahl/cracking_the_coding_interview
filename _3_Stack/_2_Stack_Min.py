# Jacob Wahl
# <Date>
#
# Problem 3.2 - How would you design a stack which, in addition to push and
#               pop, has a function min which returns the minimum element?
#               Push, pop, and min should all operate in O(1) time.
#

# The solution to this one invloves creating a stack_node class which will hold
# not only the value being inserted into the stack but the current minimum of
# the stack

from random import randint


class stack_node:

    def __init__(self, val, minimum) -> None:
        self.val = val
        self.min = minimum


class Stack:

    def __init__(self) -> None:
        self.arr = []

    def push(self, val):

        minimum = val if self.isempty() else min(val, self.minimum())

        node = stack_node(val, minimum)

        self.arr.append(node)

    def pop(self):
        if stack.isempty():
            return

        return self.arr.pop().val

    def peek(self):
        if stack.isempty():
            return

        return self.arr[len(self.arr)-1].val

    def minimum(self):
        if stack.isempty():
            return

        return self.arr[len(self.arr)-1].min

    def isempty(self):
        return False if self.arr else True

    def __str__(self) -> str:
        string = ''
        for i in self.arr:
            string += f'{i.val} '
        return string


stack = Stack()

size = 5
for _ in range(size):
    stack.push(randint(1, 10))
    print(stack)
    print(stack.minimum())

print()

while not stack.isempty():
    stack.pop()
    print(stack)
    print(stack.minimum())
