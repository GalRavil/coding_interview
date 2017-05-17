"""
Write a method to decide if two strings are anagrams or not
"""

str1 = 'abc'
str2 = 'bca'

def is_anagram_1(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram_1(str1, str2))


# collectins.Counter
from collections import Counter

def is_anagram_2(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram_2(str1, str2))


# Lists
def is_anagram_3(str1, str2):
    return list(str1).sort() == list(str2).sort()

print(is_anagram_3(str1, str2))