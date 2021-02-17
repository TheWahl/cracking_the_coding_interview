class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Linked_List:

    def __init__(self, val=None):
        self.head = None if val == None else Node(val)
        self._length = 0 if val == None else 1

    def insert(self, val, idx=0):

        n = Node(val)
        if idx == 0:  # Insert at head of list
            if self.isEmpty():
                self.head = n
            else:
                n.next = self.head
                self.head = n
        else:  # Insert at specified index
            if idx < 0:
                raise IndexError
            if idx > self._length:
                idx = self._length

            cur = self.head
            prev = None
            while idx != 0:
                prev = cur
                cur = cur.next
                idx -= 1
            n.next = prev.next
            prev.next = n

        self._length += 1

    def append(self, val):

        n = Node(val)
        if self.isEmpty():
            self.head = n
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = n

        self._length += 1

    def remove(self, idx=0):
        if self._length == 0:
            raise IndexError('List is empty!')
        elif idx >= self._length or idx < 0:
            raise IndexError('Index out of Bounds!')

        if idx == 0:  # Remove at head of list
            self.head = self.head.next
        else:  # Remove at specified index
            cur = self.head
            prev = None
            while idx != 0:
                prev = cur
                cur = cur.next
                idx -= 1
            prev.next = cur.next

        self._length -= 1

    def get(self, idx):
        if self._length == 0:
            raise IndexError('List is empty')
        elif idx >= self._length or idx < 0:
            raise IndexError('Index out of Bounds')

        cur = self.head
        while idx != 0:
            cur = cur.next
            idx -= 1
        return cur.val

    def find(self, val):
        idx = 0
        cur = self.head
        while cur != None:
            if cur.val == val:
                return idx
            else:
                cur = cur.next
                idx += 1

        return -1

    def __str__(self):
        if self.head == None:
            return 'List Empty'
        else:
            cur = self.head
            string = ''
            while cur != None:
                if cur.next != None:
                    string += f'{cur.val} -> '
                    cur = cur.next
                else:  # Last element
                    string += f'{cur.val}'
                    cur = cur.next  # breaking loop

            return string

    def __len__(self):
        return self._length

    def isEmpty(self):
        return self._length == 0
