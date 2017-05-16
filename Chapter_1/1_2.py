"""
Write code to reverse a C-Style String.
(C-Style means that "abcd" is represented as five characters, including
the null character)
"""

import unittest

def reverse_str_1(str_):
    return str_[::-1]

def reverse_str_2(str_):
    return ''.join(reversed(str_))

def reverse_str_3(str_):
    list_ = list(str_)
    list_.reverse()
    return ''.join(list_)


#using recursive method
def recursive_reverse_str(str_):
    if str_ != "":
        return str_[-1:] + recursive_reverse_str(str_[:-1])
    else: 
        return ""



class reverse_test(unittest.TestCase):
    
    TEST_DATA = [
            ('abc', 'cba'),
            ('qwerty', 'ytrewq')
            ]

    def test_reverse_str_1(self):
        for example, expected_result in self.TEST_DATA:
            result = reverse_str_1(example)
            self.assertEqual(result, expected_result)
    
    def test_reverse_str_2(self):
        for example, expected_result in self.TEST_DATA:
            result = reverse_str_2(example)
            self.assertEqual(result, expected_result)
    
    def test_reverse_str_3(self):
        for example, expected_result in self.TEST_DATA:
            result = reverse_str_3(example)
            self.assertEqual(result, expected_result)
    
    def test_recursive_reverse_str(self):
        for example, expected_result in self.TEST_DATA:
            result = recursive_reverse_str(example)
            self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()