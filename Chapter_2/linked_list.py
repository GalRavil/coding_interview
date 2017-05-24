from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
    
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, value):
        new_node = Node(value)
        
        # if the old list is none, set new node as the first node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            
#    # remove the first node that have the same value as the given node_value
#    def remove_node(self, node_value):
#        current = self.head
#        if current.value == node_value:
#            self.head = self.head.next
#        while current.next != None:
#            if current.next.value == node_value:
#                current.next = current.next.next
#                break
#            else:
#                current = current.next

    def __str__(self):
        if self.head != None:
            index = self.head
            node_store = [str(index.value)]
            
            while index.next != None:
                index = index.next
                node_store.append(str(index.value))
            
            return "[{}]".format('->'.join(node_store))
        return "[]"
                
    def value(self):
        if self.head != None:
            index = self.head
            node_store = [str(index.value)]
            
            while index.next != None:
                index = index.next
                node_store.append(str(index.value))
            
            return "[{}]".format('->'.join(node_store))
        return "[]"
    
def random_linked_list(length, min_, max_):
    linked_list = Linked_list()
    for i in range(length):
        value = randint(min_, max_)
        linked_list.add_node(value)
    return linked_list


def list_to_linked(list_):
    new_linked = Linked_list()
    for i in list_:
        new_linked.add_node(i)
    return new_linked