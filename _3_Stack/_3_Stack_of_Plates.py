# Jacob Wahl
# 3/18/21
#
# Problem 3.3 - Imagine a literal stack of plates. If the stack gets too high,
#               it might topple. Therefore, in real life, we would likely
#               start a new stack when the previous stack exceeds some
#               thershold. Implement a data strcture SetOfStacks that mimics
#               this. SetOfStacks should be composed of several stacks and
#               should create a new stack once the previous one exceeds
#               capacity SetOfStacks.push() and SetOfStacks.pop() should
#               behave identically to a single stack.
#               FOLLOW UP: Implement a function popAt(int index) which
#                          performs a pop operation on a specific sub-stack.
#

from typing import Set


class Stack:

    def __init__(self) -> None:
        self.arr = []

    def push(self, val):

        self.arr.append(val)

    def pop(self):

        if self.arr:
            return self.arr.pop()
        else:
            return None

    def peek(self):

        if self.arr:
            return self.arr[len(self.arr)-1]
        else:
            return None

    def isempty(self):
        return False if self.arr else True


class Set_of_Stacks:

    CUR_SIZE = 3

    def __init__(self) -> None:
        self.stacks = [Stack()]
        self.cur_stack_idx = 0
        self.cur_stack_len = 0

    def push(self, val):

        if self.cur_stack_len == self.CUR_SIZE:
            self.stacks.append(Stack())
            self.cur_stack_idx += 1
            self.cur_stack_len = 0

        self.stacks[self.cur_stack_idx].push(val)
        self.cur_stack_len += 1

    def pop(self):

        if self.cur_stack_len == 0:
            raise IndexError('Stack is empty')

        val = self.stacks[self.cur_stack_idx].pop()
        self.cur_stack_len -= 1

        if self.cur_stack_len == 0:
            if self.cur_stack_idx != 0:
                self.cur_stack_idx -= 1
                self.cur_stack_len = self.CUR_SIZE

        return val

    def peek(self):

        if self.cur_stack_len == 0:
            raise IndexError('Stack is empty')

        return self.stacks[self.cur_stack_idx].peek()

    def isempty(self):
        return self.cur_stack_idx == 0 and self.cur_stack_len == 0


ss = Set_of_Stacks()
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    ss.push(i)

while not ss.isempty():
    ss.peek()
    print(ss.pop())
