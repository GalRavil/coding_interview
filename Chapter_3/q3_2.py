"""
How would you design a stack which, in addition to push and pop, also
has a function  min which returns the minimum element?
Push, pop, and min should all operate in O(1) time.
"""
import random


# Use a list to store data
class Stack:
    def __init__(self, storage=[]):
        self.storage = storage

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    def get_min(self):
        return min(self.storage)


data = []
for i in range(100):
    data.append(random.randint(1, 99))

test = Stack(data)

test.push(77)

print(test.pop())
print(test.get_min())
