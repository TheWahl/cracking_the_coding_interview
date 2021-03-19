# Jacob Wahl
# <Date>
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
