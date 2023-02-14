# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class
class LinkedList:

    # constructor
    def __init__(self, value):
        new_node = Node(value) # create a first node
        self.head = new_node # assign the first one as a head
        self.tail = new_node # assign the first one as a tail
        self.length = 1 # keep track of the length

my_ll = LinkedList(4)
print(my_ll.head.value)