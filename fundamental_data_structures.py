"""
Fundamental Data Structures.

@author: agarwalnaimish
"""


class Bag(object):

    def __init__(self):
        pass

    def add(self, item):
        pass

    def is_Empty(self):
        pass

    def size(self):
        pass


class Queue(object):

    def __init__(self):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


class FixedCapacityStack(object):

    def __init__(self, capacity, auto_resize_capacity=False):

        # _ds is acronym for underlying data structure
        self._ds = []
        self._capacity = capacity
        self._count = 0
        self._auto_resize_capacity = auto_resize_capacity

    def push(self, item):

        if self._count < self._capacity:
            self._ds.append(item)
            self._count += 1
        elif self._auto_resize_capacity:
            self.resize(self._capacity * 2)
            self._ds.append(item)
            self._count += 1

    def pop(self):

        if not self.is_empty():
            self._count -= 1
            value = self._ds[self._count]
            self._ds[self._count] = None

            if self._auto_resize_capacity:
                if self._count < (self._capacity / 4):
                    self.resize(self._capacity / 2)

            return value

    def is_empty(self):
        return self._count == 0

    def size(self):
        return self._count

    def resize(self, new_capacity):
        if new_capacity > self._count:
            self._capacity = new_capacity
