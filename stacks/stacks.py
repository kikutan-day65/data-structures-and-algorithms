class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node()   # initialize the node
        self.top = new_node # set the top of stack
        self.heght = 1  # keep track of length of stack
    