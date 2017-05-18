"""
Assume you have a method is_substring which checks if one word is a 
substring of another. Given two strings, s1 and s2.
Write code to check if s2 is a rotation of s1 using only one call 
to is_substring.
(i.e.  "waterbottle" is rotation of "erbottlewat")
"""

s1 = "waterbottle"
s2 = "erbottlewat"


def is_substring(s1, s2):
    return s1 == s2


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    list1 = sorted(list(s1))
    list2 = sorted(list(s2))

    return is_substring(list1, list2)


if is_rotation("waterbottle", "erbottlewat"):
    print("Test 1 Passed")

if not is_rotation("waterbottle", "nope"):
    print("Test 2 Passed")

if not is_rotation("waterbottlewater", "waterbottle"):
    print("Test 3 Passed")