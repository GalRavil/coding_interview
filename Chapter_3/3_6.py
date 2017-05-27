"""
Write a program to sort a stack in ascending order. You should not make any
assumptions about how the stack is implemented. The following are the only
functons that should be used to write this program:
 push | pop | peek | is_empty
"""
import unittest


# implementation of Stack with push, pop, peek, is_empty methods
class Stack:
    # push -> first stack
    # pop <- second stack
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        # instead of append using extend method to insert 
        # iterable data
        self.stack.extend(value)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0

    # to sort stack in ascending order
    # this is the easiest way...
    def sort(self):
        self.stack.sort()
    # but let's make our life a little more difficult
#    def sort(self):
        

# ========== Test =============
class Test_stack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        data = [*range(10)]
        data = data[::-1]  # reverse
        self.stack.push(data)
    
    def test_sort(self):
        expected = [x for x in range(10)]
        self.stack.sort()
        self.assertEqual(self.stack.stack, expected)


if __name__ == '__main__':
    unittest.main()
