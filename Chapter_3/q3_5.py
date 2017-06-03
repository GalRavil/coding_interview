"""
Implement a My_queue class which implements a queue using two stacks.
"""
class MyQueue:
    # push -> zero stack
    # pop <- first stack
    def __init__(self):
        self.st = [[], []]
    
    def push(self, value):
        if len(value) == 1:
            self.st[0].append(value)
        # if given value consists of multiple elements
        # from top to bottom ---->
        else:
            self.st[0].extend(value)
    
    def pop_(self):
        if self.st[1]:
            
            return self.st[1].pop()
        
        # throw over from 1st to 2nd stack
        while self.st[0]:
            self.st[1].append(self.st[0].pop())
        
        return self.st[1].pop()



# ======= Test =========
import unittest


class Test_MyQueue(unittest.TestCase):
    def setUp(self):
        self.queue = MyQueue()

    def test_push(self):
        data = [*range(5)]
        self.queue.push(data)
        res = self.queue.st
        expected = [[0, 1, 2, 3, 4], []]
        self.assertEqual(res, expected)

    def test_pop_one_value(self):
        self.queue.st = [[4, 5], [1, 2]]
        result = self.queue.pop_()
        self.assertEqual(result, 2)

    def test_popped_stacks(self):
        self.queue.st = [[1, 2, 3], []]
        self.queue.pop_()
        result = self.queue.st
        expected = [[], [3, 2]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
