class HashTable:
    # hash constructor = it creates an address space
    def __init__(self, size = 7):
        self.data_map = [None] * size # set the default size of hash table
    
    """
    why 7?:
            a PRIME number increases the amount of randomness
            how the key value pairs are gonna be distributed through the hash table.
            it reduces the collision.
    """
    
    #=====================================================================================================

    # hash method
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    """
    why 23? = it's a prime number. you can put it any prime number instead.

    % len(self.data_map) = returns the remainder 0 ~ 6 if self.data_map = 7 (default)
                           it is teh exactly our address space 

    ord() = returns an integer representing the Unicode character.
    ex:
        character = 'P'
        unicode_char = ord(character)
        print(unicode_char)

        # Output: 80
    """

    #=====================================================================================================

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    #=====================================================================================================




my_hash_table = HashTable()
my_hash_table.print_table()