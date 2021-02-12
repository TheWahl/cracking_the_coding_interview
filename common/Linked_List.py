class Node:
    def __init__(self, val):
        self._val = val
        self._next = None


class LinkedList:

    def __init__(self, val=None):
        self._head = None if val == None else Node(val)
        self._length = 0 if val == None else 1

    def insert(self, val, idx=0):

        n = Node(val)
        if idx == 0:  # Insert at head of list
            n._next = self._head
            self._head = n
        else:
            if idx >= self._length or idx < 0:
                raise IndexError('Index out of Bounds')

            if idx == 0:  # Insert at head of list
                n._next = self._head
                self._head = n
            else:  # Insert at specified index
                cur = self._head
                prev = None
                while idx != 0:
                    prev = cur
                    cur = cur._next
                    idx -= 1
                n._next = prev._next
                prev._next = n

        self._length += 1

    def remove(self, idx=0):
        if self._length == 0:
            raise IndexError('List is empty')
        elif idx >= self._length or idx < 0:
            raise IndexError('Index out of Bounds')

        if idx == 0:  # Remove at head of list
            self._head = self._head._next
        else:  # Remove at specified index
            cur = self._head
            prev = None
            while idx != 0:
                prev = cur
                cur = cur._next
                idx -= 1
            prev._next = cur._next

        self._length -= 1

    def get(self, idx):
        if self._length == 0:
            raise IndexError('List is empty')
        elif idx >= self._length or idx < 0:
            raise IndexError('Index out of Bounds')

        cur = self._head
        while idx != 0:
            cur = cur._next
            idx -= 1
        return cur._val

    def find(self, val):
        cur = self._head
        while cur._next != None:
            if cur._val == val:
                return True
            else:
                cur = cur._next
        return False

    def __str__(self):
        if self._head == None:
            return 'List Empty'
        else:
            cur = self._head
            string = ''
            while cur._next != None:
                string += f'{cur._val} -> '
                cur = cur._next
            else:
                string += f'{cur._val}'
            return string

    def __len__(self):
        return self._length

    def isEmpty(self):
        return self._length == 0
