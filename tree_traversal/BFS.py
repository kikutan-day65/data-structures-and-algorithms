class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
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


    # =====================================================================================================

    def BFS(self):

        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:

            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
                
        return results


bfs_tree = Tree()
bfs_tree.insert(32)
bfs_tree.insert(4)
bfs_tree.insert(12)
bfs_tree.insert(76)
bfs_tree.insert(39)
bfs_tree.insert(11)
bfs_tree.insert(7)

print(bfs_tree.BFS())