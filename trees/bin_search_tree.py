class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None    # top-most node of the bin search tree

    #=====================================================================================================

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        
        while True:
            if new_node.value == temp.value:
                return False
        
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
        
                temp = temp.left
        
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
        
                temp = temp.right


    """
    STEPs for inserting:
        create new_node
        if root == None then root = new_node
        temp = self.root
        while loop:
            if new_node == temp return False
            if '<' go left, else '>' go right
            if None insert new_node, else move to next
    """
    #=====================================================================================================



my_tree = BinarySearchTree()
print(my_tree.root)

print()

insert_tree = BinarySearchTree()
insert_tree.insert(2)
insert_tree.insert(1)
insert_tree.insert(3)

print('Root:', insert_tree.root.value)            
print('Root->Left:', insert_tree.root.left.value)        
print('Root->Right:', insert_tree.root.right.value)

print()