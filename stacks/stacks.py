class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)   # initialize the node
        self.top = new_node # set the top of stack
        self.height = 1  # keep track of length of stack

    #=====================================================================================================

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #=====================================================================================================

    def push(self, value):
        new_node = Node(value)

        # when the stack is empty
        if self.height == 0:
            self.top = new_node
            self.height += 1
        
        # otherwise
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
    
    #=====================================================================================================



my_stack = Stack(4)
my_stack.print_stack()

print()

push_stack = Stack(3)
push_stack.push(12)
push_stack.push(15)
push_stack.push(2)
push_stack.print_stack()