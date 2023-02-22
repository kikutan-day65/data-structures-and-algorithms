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
    STEPs to insert:
        create new_node
        if root == None then root = new_node
        temp = self.root
        while loop:
            if new_node == temp return False
            if '<' go left, else '>' go right
            if None insert new_node, else move to next
    """

    #=====================================================================================================

    def contains(self, value):
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right
            
            else:
                return True
        
        return False


    """
    STEPs to check contain
        if root == None return False
        temp = self.root
        while temp is not None:
            if '<' go left
            elif '>' go right
            else: return True
        return False
    """


    #=====================================================================================================

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    #=====================================================================================================

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)


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

contain_tree = BinarySearchTree()
contain_tree.insert(21)
contain_tree.insert(15)
contain_tree.insert(30)
contain_tree.insert(67)
contain_tree.insert(12)
contain_tree.insert(77)
contain_tree.insert(32)
print(contain_tree.contains(67))
print(contain_tree.contains(9))

print()

r_bst_contain = BinarySearchTree()
r_bst_contain.insert(47)
r_bst_contain.insert(21)
r_bst_contain.insert(76)
r_bst_contain.insert(18)
r_bst_contain.insert(27)
r_bst_contain.insert(53)
r_bst_contain.insert(82)

print('BST Contains: 27: ')
print(r_bst_contain.r_contains(27))

print('BST Contains: 17: ')
print(r_bst_contain.r_contains(17))

print()
r_bst_insert = BinarySearchTree()
r_bst_insert.insert(2)
r_bst_insert.insert(1)
r_bst_insert.insert(3)

print('Root: ', r_bst_insert.root.value)
print('Root -> Left: ', r_bst_insert.root.left.value)
print('Root -> Right: ', r_bst_insert.root.right.value)