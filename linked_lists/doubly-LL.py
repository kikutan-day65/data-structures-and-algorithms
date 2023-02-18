# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# DoublyLinkedList class
class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #=====================================================================================================

    def print_list(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    #=====================================================================================================
    
    def append(self, value):
        new_node = Node(value)

        # when the doubly linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # otherwise
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1

        return True

    #=====================================================================================================

    def pop(self):
        
        # when the doubly linked list is empty
        if self.length == 0:
            return None
        
        temp = self.tail

        # when the doubly linked list has only one item
        if self.length == 1:
            self.head = None
            self.tail = None
        
        # otherwise
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1

        return temp
    
    #=====================================================================================================

    def prepend(self, value):
        new_node = Node(value)

        # when th doubly linked list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        # otherwise
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

        return True
    
    #=====================================================================================================
    
    def pop_first(self):
        
        # when the doubly linked list is empty
        if self.length == 0:
            return None
        
        temp = self.head
        
        # when the doubly linked list has only one item
        if self.length == 1:
            self.head = None
            self.tail = None
        
        # otherwise
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1

        return temp
    
    #=====================================================================================================

    def get(self, index):

        # check if the index is valid
        if index < 0 or index >= self.length:
            return False
        
        temp = self.head

        # when the index is near from head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        
        # when the index is near from tail
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        
        return temp # to use set_value() return this, but to use only get() return temp.value
    
    """
    to get a specific node in doubly linked list, we can optimize the code
    depending on which head/tail the node is near from 
    """

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
        if index < 0 or index >= self.length:
            return False
        
        # when the index is 0
        if index == 0:
            return self.prepend(value)
        
        # when the index = lenght of doubly linked list
        if index == self.length:
            return self.append(value)
        
        # otherwise
        new_node = Node(value)

        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
             
        self.length += 1

        return True
    
    #=====================================================================================================

    def remove(self, index):

        # check if the index is valid
        if index < 0 or index >= self.length:
            return False
        
        # when the index is 0
        if index == 0:
            return self.pop_first()
        
        # when the index = lenght of doubly linked list
        if index == self.length:
            return self.pop()
        
        # otherwise
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        
        return temp


doubly_LL = DoublyLinkedList(7)
doubly_LL.print_list()

print()

append_doubly_LL = DoublyLinkedList(2)
append_doubly_LL.append(3)
append_doubly_LL.append(4)
append_doubly_LL.print_list()

print()

pop_doubly_LL = DoublyLinkedList(7)
pop_doubly_LL.append(8)
pop_doubly_LL.append(9)
pop_doubly_LL.pop()
pop_doubly_LL.print_list()

print()

prepend_doubly_LL = DoublyLinkedList(7)
prepend_doubly_LL.append(8)
prepend_doubly_LL.append(9)
prepend_doubly_LL.prepend(10)
prepend_doubly_LL.print_list()

print()

pop_first_doubly_LL = DoublyLinkedList(1)
pop_first_doubly_LL.append(2)
pop_first_doubly_LL.append(3)
pop_first_doubly_LL.pop_first()
pop_first_doubly_LL.print_list()

print()

get_doubly_LL = DoublyLinkedList(4)
get_doubly_LL.append(5)
get_doubly_LL.append(6)
print(get_doubly_LL.get(0))

print()

set_value_doubly_LL = DoublyLinkedList(3)
set_value_doubly_LL.append(4)
set_value_doubly_LL.append(5)
set_value_doubly_LL.set_value(1, 23)
set_value_doubly_LL.print_list()

print()

insert_doubly_LL = DoublyLinkedList(5)
insert_doubly_LL.append(6)
insert_doubly_LL.append(7)
insert_doubly_LL.insert(0, 12)
insert_doubly_LL.print_list()

print()

remove_doubly_LL = DoublyLinkedList(7)
remove_doubly_LL.append(8)
remove_doubly_LL.append(9)
remove_doubly_LL.append(10)
remove_doubly_LL.remove(2)
remove_doubly_LL.print_list()