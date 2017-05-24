"""
You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1st 
digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as
a linked list.

Ex: input: [3->1->5]+[5->9->2]
    output: [8->0->8]
"""

from linked_list import *
import unittest

test_list1 = list_to_linked([2, 1, 5])
print(test_list1)

test_list2 = list_to_linked([5, 9, 2])
print(test_list2)


class Add_linked_lists:
    def __init__(self, linked1, linked2):
        self.linked1 = linked1
        self.linked2 = linked2
    
    def main(self):
        num1 = self._linked_to_num(self.linked1)
        num2 = self._linked_to_num(self.linked2)
        
        total = num1 + num2
        
        sum_list = list(str(total))
        sum_list.reverse()
               
        sum_linked = self._list_to_linked(sum_list)
        return sum_linked
        
    def _linked_to_num(self, linked):
        num_list = []
        
        current_node = linked.head
        
        while current_node != None:
            num_list.append(current_node.value)
            current_node = current_node.next
               
        #inplace reversion
        num_list.reverse()
        
        num = ''.join(map(str, num_list))
        return int(num)
    
    def _list_to_linked(self, list_):
        new_linked = Linked_list()
        for i in list_:
            new_linked.add_node(i)
        return new_linked
    
    
test = Add_linked_lists(test_list1, test_list2)
print(test.main())




# ===== Test ======

test_linked1 = list_to_linked([1, 2, 3])
test_linked2 = list_to_linked([4, 5, 6])

result = Add_linked_lists(test_linked1, test_linked2).main()
expected = list_to_linked([5, 7, 9])
wrong = list_to_linked([1, 1, 1])


class Test_linked(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(result.value(), expected.value())
    
    def test_not_equal(self):
        self.assertNotEqual(result.value(), wrong.value())

if __name__ == "__main__":
    unittest.main()



