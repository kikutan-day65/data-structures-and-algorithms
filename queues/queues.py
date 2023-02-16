class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    #=====================================================================================================

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    #=====================================================================================================
    
    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
            self. length += 1

        else:
            self.last.next = new_node
            new_node = self.last
            self.length += 1

    #=====================================================================================================


my_queue = Queue(5)
my_queue.print_queue()

print()

en_queue = Queue(3)
en_queue.enqueue(4)
en_queue.enqueue(5)
en_queue.print_queue()
