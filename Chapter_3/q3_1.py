"""
Describe how you could use a single array to implement three stacks.
"""

# using nested lists
class Single_array_stack:
    def __init__(self, stack_size=100, number=3):
        self.stack_size = stack_size
        self.number = number
        self.array = [None] * self.stack_size * self.number
        self.pointer = [-1] * self.number

    def push(self, stack_num, value):
        if self.pointer[stack_num] + 1 >= self.stack_size:
            print('Out of space')
        else:
            self.pointer[stack_num] += 1
            self.array[self.stack_top(stack_num)] = value
    
    def pop(self, stack_num):
        if self.pointer[stack_num] < 0:
            return 'Trying to pop an empty stack'
        else:
            data = self.array[self.stack_top(stack_num)]
            self.array[self.stack_top(stack_num)] = None
            self.pointer[stack_num] -= 1
            return data
    
    def peek(self, stack_num):
        if self.pointer[stack_num] < 0:
            print('Empty stack')
        else:
            return self.array[self.stack_top(stack_num)]
    
    def is_empty(self, stack_num):
        return self.pointer[stack_num] == -1
    
    def stack_top(self, stack_num):
        return self.stack_size * stack_num + self.pointer[stack_num]


# ===================  Test  =====================
if __name__ == '__main__':
    array = Single_array_stack()
    array.push(2, 11)
    array.push(2, 13)
    print(array.pop(0))  # Trying to pop an empty stack
    print(array.peek(2))  # 13
    array.push(0, 20)
    array.push(0, 30)
    print(array.pop(0))  # 30
    print(array.peek(0))  # 20
