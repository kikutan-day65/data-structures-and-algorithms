class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    # =====================================================================================================

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
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

    # =====================================================================================================
       
    def DFS_preorder(self):
        results = []

        def traverse(current_node):

            results.append(current_node.value)

            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    # =====================================================================================================

    def DFS_postorder(self):
        results = []

        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)
            
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    # =====================================================================================================
    
    def DFS_inorder(self):
        results = []

        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)

            results.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results



dfs_tree = Tree()
dfs_tree.insert(47)
dfs_tree.insert(21)
dfs_tree.insert(76)
dfs_tree.insert(18)
dfs_tree.insert(27)
dfs_tree.insert(52)
dfs_tree.insert(82)

print('Pre-order: ', dfs_tree.DFS_preorder())

print()

print('Post-order: ', dfs_tree.DFS_postorder())

print()

print('In-order: ', dfs_tree.DFS_inorder())