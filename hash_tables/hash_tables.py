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

    # hash method = it determines the address for incoming key
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    """
    why 23? = it's a prime number. you can put it any prime number instead.

    % len(self.data_map) = returns the remainder 0 ~ 6 if self.data_map = 7 (default)
                           it's the exactly our address space 

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

    def set_item(self, key, value):
        index = self.__hash(key)    # computing an address here
        
        # initialize the empty list i the value part of the hash table
        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])

    #=====================================================================================================

    def get_item(self, key):
        index = self.__hash(key)
        
        if self.data_map is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
    #=====================================================================================================



hash_table = HashTable()
hash_table.print_table()

print()

set_hash = HashTable(11)
set_hash.set_item("haruto", 25)
set_hash.set_item("yazan", 19)
set_hash.set_item("yuta", 23)
set_hash.set_item("hiro", 24)
set_hash.print_table()

print()

get_hash = HashTable()
get_hash.set_item("cookie", 1000)
get_hash.set_item("water", 120)
print(get_hash.get_item("cookie"))
print(get_hash.get_item("water"))
print(get_hash.get_item("tissue"))

print()