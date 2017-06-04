# implementation of binary tree for 4th chapter


class BinaryNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, val):
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)
    
    def delete(self):
        """
        works in conjunction with remove method in BinaryTree
        """
        if self.left == self.right is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left
        
        child = self.left
        grandchild = child.right
        
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value
        
        return self
        

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    
    def contains(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        
        return False
    
    def remove(self, value):
        if self.root:
            self.root = self.remove_from_parent(self.root, value)
    
    def remove_from_parent(self, parent, value):
        if parent is None:
            return None
        
        if value == parent.value:
            return parent.delete()
        elif value < parent.val:
            parent.left = self.remove_from_parent(parent.left, value)
        else:
            parent.right = self.remove_from_parent(parent.right, value)
        
        return parent
