class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        """
        Finds the middle node of the linked list using the 
        "slow and fast pointers" technique.
 
        Returns:
        - If the length of the linked list is even, returns the second middle node.
        - If the length of the linked list is odd, returns the middle node.
 
        Time complexity: O(n)
        Space complexity: O(1)
        """
        # Initialize two pointers, slow and fast, to the head of the linked list
        slow = self.head
        fast = self.head
 
        # Move the fast pointer two nodes ahead for every one node that the slow pointer moves ahead
        # When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
 
        # Return the middle node
        return slow



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""