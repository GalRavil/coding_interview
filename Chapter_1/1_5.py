"""
Write a method to replace all spaces in a string with '%20'
"""



str_ = 'Hello my little friend!'

def replace1(str_):
    return str_.replace(' ', '%20')

print(replace1(str_))



# using a list to store each char and change space to '%20', 
# then join list into a string
def replace2(str_):
    chars_list = []
    
    for ch in str_:
        if ch == ' ':
            ch = '%20'
        chars_list.append(ch)
    
    return ''.join(chars_list)

print(replace2(str_))


def replace3(str_):
    return '%20'.join(str_.split())

print(replace3(str_))



# re.sub
import re

def replace4(str_):
    return re.sub(r"\s+", '%20', str_)

print(replace4(str_))