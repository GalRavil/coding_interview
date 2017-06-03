"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the 
previous stack exceeds some threshold.
Implement a data structure Set_of_stacks that mimics this. Set_of_stacks
should be composed of several stack, and should create a new stack once
the previous one exceeds capacity.
Set_of_stacks.push() and Set_of_stacks.pop() should behave identically
to a single stack (that is, pop() should return should return the same
values as it would if there were a single stack).

Follow up: implement a function pop_at(int index) which performs a pop
operation on a specific sub-track.
"""
class Set_of_stacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def push(self, value):
        # if if there is no stacks yet or the last one is already full
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)
    
    def pop(self):
        # if there is no stacks yet
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()

        # pop the last stack if it's empty
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data

    # index begins from 0.
    # makes chosen stacks not at full capacity.
    def pop_at(self, index):
        # if index out of range or chosen stack is empty
        if index > len(self.stacks) or len(self.stacks[index]) == 0:
            return None
        return self.stacks[index].pop()



# ======= Test =========
import unittest


class Test_Set(unittest.TestCase):
    def setUp(self):
        self.set = Set_of_stacks(5)
        self.set.stacks = [[6, 8, 3, 9, 6], [8]]

    def test_push(self):
        data = [2, 8, 2, 10, 4, 7, 6]
        expected = [[6, 8, 3, 9, 6], [8, 2, 8, 2, 10], [4, 7, 6]]

        for i in data:
            self.set.push(i)
        self.assertEqual(self.set.stacks, expected)

    def test_pop(self):
        expected = [[6, 8, 3, 9]]

        self.set.pop()
        self.set.pop()

        self.assertEqual(self.set.stacks, expected)

    def test_pop_at(self):
        expected = [[6, 8, 3, 9], [8]]
        self.set.pop_at(0)
        self.assertEqual(self.set.stacks, expected)

if __name__ == '__main__':
    unittest.main()
