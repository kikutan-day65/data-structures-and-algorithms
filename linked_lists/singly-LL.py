# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# LinkedList class
class LinkedList:

    def __init__(self, value):
        new_node = Node(value)  # create a first node
        self.head = new_node    # assign the first one as a head
        self.tail = new_node    # assign the first one as a tail
        self.length = 1     # keep track of the length
    

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
    

    def append(self, value):
        new_node = Node(value)  # create a new node object

        # when the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # otherwise
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True


    def pop(self):
        # when the linked list is empty
        if self.length == 0:
            return None
        
        # otherwise
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # when the linked list has only one item
        # length should be 0 after the popping an item
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp # return popped an item



append_ll = LinkedList(4)
append_ll.append(2)
append_ll.print_list()

print()

pop_ll = LinkedList(12)
pop_ll.append(5)
pop_ll.append(9)
pop_ll.append(6)
pop_ll.pop()
pop_ll.print_list()