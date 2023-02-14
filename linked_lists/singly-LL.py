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
            print(temp.value, end=" ")   # print
            temp = temp.next    # assign temp to the next value
    

    # append
    def append(self, value):
        new_node = Node(value)  # create a new node object

        # when the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # otherwise
        else:
            self.tail.next = new_node   # point new_node as a next node
            self.tail = new_node    # change the tail node
        
        self.length += 1    # increment the length
        return True


my_ll = LinkedList(4)

my_ll.append(2)
my_ll.print_list()