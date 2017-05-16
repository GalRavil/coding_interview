"""
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?
"""

import unittest

def all_unique(str_):
    return len(str_) == len(set(str_))


#This will actually be more efficient if the string is large and there are 
#duplicates early, because it will short-circuit (exit as soon as the 
#first duplicate is found)
def unique(str_):
    unique_chars = set()
    
    for ch in str_:
        if ch in unique_chars:
            return False
        unique_chars.add(ch)
        
    return True


#without using additional data structures
def without_structures(str_):
    for ch in str_:
        if str_.count(ch) > 1:
            return False
    return True


func_list = [all_unique, unique, without_structures]


class all_unique_test(unittest.TestCase):
    
    TEST_DATA = [
        ('a', True),
        ('aa', False),
        ('ab', True), 
        ('ab ', True), 
        ('', True),
        (' ', True),
        ('  ', False),
        ('qwerty', True),
        ]
    
    def test_functions(self):
        for func in func_list:
            for example, expected_result in self.TEST_DATA:
                result = func(example)
                self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()