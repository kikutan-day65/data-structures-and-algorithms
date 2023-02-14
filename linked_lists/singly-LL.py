# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class
class LinkedList:

    # constructor
    def __init__(self, value):
        new_node = Node(value)  # create a first node
        self.head = new_node    # assign the first one as a head
        self.tail = new_node    # assign the first one as a tail
        self.length = 1     # keep track of the length
    
    # print linked list
    def print_list(self):
        temp = self.head    # assign the first node to temp
        while temp is not None: # loop until temp reaches None
            print(temp.value)   # print
            temp = temp.next    # assign temp to the next value

my_ll = LinkedList(4)
print(my_ll.head.value)