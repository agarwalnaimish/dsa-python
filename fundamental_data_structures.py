"""

Fundamental Data Structures.

@author: Naimish Agarwal

"""

from numba import jit


class ArrayStack(object):

    @jit
    def __init__(self, capacity, auto_resize_capacity=False):

        self._capacity = capacity

        # _ds is acronym for underlying data structure
        self._ds = [None] * self._capacity

        self._count = 0
        self._auto_resize_capacity = auto_resize_capacity

    @jit
    def push(self, item):

        if self._count < self._capacity:
            self._ds[self._count] = item
            self._count += 1
        elif self._auto_resize_capacity:
            self.resize(self._capacity * 2)
            self._ds[self._count] = item
            self._count += 1
        else:
            raise BaseException("StackOverflowException")

    @jit
    def pop(self):

        if not self.is_empty():
            self._count -= 1
            value = self._ds[self._count]
            self._ds[self._count] = None

            if self._auto_resize_capacity:
                if self._count < (self._capacity / 4):
                    self.resize(self._capacity / 2)

            return value
        else:
            raise BaseException("StackUnderflowException")

    @jit
    def is_empty(self):
        return self._count == 0

    @jit
    def size(self):
        return self._count

    @jit
    def resize(self, new_capacity):
        if new_capacity >= self._count:
            self._capacity = new_capacity
        else:
            raise BaseException("StackItemsLossException")


class SinglyLinkedNode(object):

    @jit
    def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node


class LinkedListStack(object):

    @jit
    def __init__(self):
        self._top = None
        self._count = 0

    @jit
    def push(self, item):
        if self.is_empty():
            node = SinglyLinkedNode(item, None)
            self._top = node
            self._count += 1
        else:
            node = SinglyLinkedNode(item, self._top)
            self._top = node
            self._count += 1

    @jit
    def pop(self):
        if not self.is_empty():
            top = self._top
            value = top.item
            self._top = top.next_node
            del top
            self._count -= 1
            return value
        else:
            raise BaseException("StackUnderflowException")

    @jit
    def size(self):
        return self._count

    @jit
    def is_empty(self):
        return self._count == 0


class LinkedListBag(object):

    @jit
    def __init__(self):
        self._top = None
        self._count = 0

    @jit
    def add(self, item):
        if self.is_empty():
            node = SinglyLinkedNode(item, None)
            self._top = node
            self._count += 1
        else:
            node = SinglyLinkedNode(item, self._top)
            self._top = node
            self._count += 1

    @jit
    def size(self):
        return self._count

    @jit
    def is_empty(self):
        return self._count == 0

    @jit
    def iterator(self):
        node = self._top
        while node is not None:
            yield node.item
            node = node.next_node


class LinkedListQueue(object):

    @jit
    def __init__(self):
        self.first = None
        self.last = None
        self._count = 0

    @jit
    def enqueue(self, item):
        if self.is_empty():
            node = SinglyLinkedNode(item, None)
            self.first = node
            self.last = node
            self._count += 1
        else:
            node = SinglyLinkedNode(item, None)
            self.last.next_node = node
            self.last = node
            self._count += 1

    @jit
    def dequeue(self):
        if not self.is_empty():
            node = self.first
            value = node.item
            self.first = node.next_node
            self._count -= 1
            del node
            if self.is_empty():
                self.last = None
            return value
        else:
            raise Exception("QueueUnderflowException")

    @jit
    def is_empty(self):
        return self._count == 0



    def size(self):
        return self._count
