# Jacob Wahl
# <Date>
#
# Problem 3.1 - Describe how you could use a single array to implement three
#               stacks.
#

# The basic method would be to disect the array into three parts with the
# disection going as follows. If i is an index in the array then if i % 3 == 0,
# it belongs to stack 1, if i % 3 == 1, it belongs to stack 2, and if
# i % 3 == 2, it belongs to stack 2

from random import randint


class Three_Stack:

    stack1 = None
    stack2 = None
    stack3 = None
    arr = [0]

    def __init__(self) -> None:
        self.size = 0

    @classmethod
    def Stack1(cls):
        if cls.stack1 == None:
            cls.stack1 = Three_Stack()
        return cls.stack1

    @classmethod
    def Stack2(cls):
        if cls.stack2 == None:
            cls.stack2 = Three_Stack()
        return cls.stack2

    @classmethod
    def Stack3(cls):
        if cls.stack3 == None:
            cls.stack3 = Three_Stack()
        return cls.stack3

    def __compute_index(self):
        if self == Three_Stack.stack1:
            index = self.size * 3 + 0
        elif self == Three_Stack.stack2:
            index = self.size * 3 + 1
        else:
            index = self.size * 3 + 2

        return index

    def push(self, item):

        # Computing which index to insert item at
        index = self.__compute_index()

        # Determining if array needs to be enlarged to hold new item
        if index > len(self.arr) - 1:
            self.arr.extend([0] * len(self.arr))

        # Inserting item and incrementing size
        self.arr[index] = item

        self.size += 1

    def pop(self):

        if self.size == 0:
            raise IndexError('Stack is empty')

        self.size -= 1

        index = self.__compute_index()

        return self.arr[index]

    def peek(self):

        index = self.__compute_index()

        return self.arr[index]

    def isEmpty(self):

        return True if self.size == 0 else False


stack1 = Three_Stack.Stack1()
stack2 = Three_Stack.Stack2()
stack3 = Three_Stack.Stack3()

size = 3
for i in [1, 4, 7]:
    stack1.push(i)
    stack2.push(i+1)
    stack3.push(i+2)

for _ in range(size):
    print(stack1.pop())
    print(stack2.pop())
    print(stack3.pop())
