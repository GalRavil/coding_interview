"""
Implenent an algorithm to find the nth to last element of singly 
linked list.
"""
from linked_list import random_linked_list


def nth_to_last(linked, n):
    if n <= 0:
        return "invalid number!"
    pointer2 = linked.head
    
    # to check whether 'n' exceed the length  of linked_list
    for i in range(n-1):
        if pointer2.next != None:
            pointer2 = pointer2.next
        else:
            return "'n' exceeds the length of linked_list"
    
    # find out the required element
    pointer1 = linked.head
    while pointer2.next != None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
        
    return pointer1
   

#---------------test------------------
L = random_linked_list(8, 0, 100)
print(L)
print("The 3th to last element is:", nth_to_last(L, 3))
