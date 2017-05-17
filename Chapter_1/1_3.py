"""
Decide an algorithm and write code to remove the duplicate characters
in string without using any additional buffer.

Note: one or two additional variables are fine, an extera copy of the
array is not.

Follow up: write test cases for this method.
"""

str_ = 'aaabbcdefff'

# if order dosn't matter
print( ''.join(set(str_)))


# if order does matter
# collections.OrderedDict
from collections import OrderedDict
print( ''.join(OrderedDict.fromkeys(str_)))


# itertools.groupby
from itertools import groupby
print(''.join(key for key, group in groupby(str_)))