# Node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# LinkedList class
class LinkedList:

    def __init__(self, value):
        new_node = Node(value)  # create a first node
        self.head = new_node    # assign the first one as a head
        self.tail = new_node    # assign the first one as a tail
        self.length = 1     # keep track of the length
    
    #=====================================================================================================

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
    
    #=====================================================================================================

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

    #=====================================================================================================

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

    #=====================================================================================================

    def prepend(self, value):
        new_node = Node(value)

        # when the linked list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        # otherwise
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True
    
    #=====================================================================================================

    def pop_first(self):
        # when the linked list is empty
        if self.length == 0:
            return None

        # otherwise
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # when the linked list has only one item
        # length should be 0 after the popping the first item
        if self.length == 0:
            self.tail = None
        
        return temp

    #=====================================================================================================

    def get(self, index):
        # check if the index is valid
        if index < 0 or index >= self.length:
            return None

        # otherwise
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp # to use set_value() return this, but to use only get() return temp.value

    #=====================================================================================================

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False

    #=====================================================================================================

    def insert(self, index, value):
        # check if the index is valid
        if index < 0 or index > self.length:
            return False

        # when the index is 0
        if index == 0:
            return self.prepend(value)
        
        # when the index is equal to the length of linked list
        if index == self.length:
            return self.append(value)
        
        # otherwise
        new_node = Node(value)

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1

        return True
    
    #=====================================================================================================

    def remove(self, index):
        # check if the index is valid
        if index < 0 or index >= self.length:
            return None
        
        # when the index is 0
        if index == 0:
            return self.pop_first()
        
        # when the index is equal to the last item
        if index == self.length - 1:
            return self.pop()
        
        # otherwise
        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        
        self.length -= 1

        return temp

    #=====================================================================================================


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

print()

prepend_ll = LinkedList(1)
prepend_ll.append(7)
prepend_ll.append(8)
prepend_ll.prepend(3)
prepend_ll.print_list()

print()

pop_first_ll = LinkedList(3)
pop_first_ll.append(4)
pop_first_ll.append(5)
pop_first_ll.pop_first()
pop_first_ll.print_list()

print()

get_ll = LinkedList(7)
get_ll.append(8)
get_ll.append(9)
get_ll.append(10)
print(get_ll.get(2))

print()

set_value_ll = LinkedList(3)
set_value_ll.append(4)
set_value_ll.append(5)
set_value_ll.set_value(1, 23)
set_value_ll.print_list()

print()

insert_ll = LinkedList(7)
insert_ll.append(8)
insert_ll.append(9)
insert_ll.insert(2, 43)
insert_ll.print_list()

print()

remove_ll = LinkedList(7)
remove_ll.append(8)
remove_ll.append(9)
remove_ll.append(10)
remove_ll.remove(2)
remove_ll.print_list()