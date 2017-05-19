"""
Write code to remove duplicates from an unresolved linked list.
Follow up: how would you solve this problem if a temporary buffer is not
allowed?
"""

from linked_list import *


# use a hash table, O(n)
def delete_dups(list_):
    if list_.head != None:
        current_node = list_.head
        dic = {current_node.value: True}
               
        while current_node.next != None:
            if current_node.next.value in dic:
                current_node.next = current_node.next.next
            else:
                dic[current_node.value] = True
                current_node = current_node.next


#==========
L1 = random_linked_list(9,3,7)
print(L1)

delete_dups(L1)
print(L1)
#==========


# if temporary buffer is not allowed (no additional data structure)
def delete_dups2(list_):
    current_node = list_.head
    while current_node != None:
        runner = current_node
        while runner.next != None:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next


#====
L2 = random_linked_list(9, 3, 7)
print(L2)

delete_dups2(L2)
print(L2)
#====








