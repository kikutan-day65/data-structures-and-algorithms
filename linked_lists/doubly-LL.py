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