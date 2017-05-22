"""
Implement an algorithm to delete a node in the middle of a single linked
list, given only access to that node.

Ex: input: List[a->b->c->d->e]
    result: nothing is returned, but the new linked list looks like [a->b->d->e]
"""

from linked_list import random_linked_list


def delete_node(link_list, node):
    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next
    
    # if the given node is the last one
    else:
        node.value = None



# Test
test_list = random_linked_list(5, 0, 10)

# give acces to the 3rd node
node = test_list.head.next.next

print(test_list)

delete_node(test_list, node)
print('After...')
print(test_list)