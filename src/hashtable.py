# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        
        # Basic insertion plan:
        # create a new variable with the hashed key argument 
        # check if hashed key exists:
            # if yes send an error
            # else add the value to the hashtable array through 
            # the command self.storage[hashed_key] = value 

        hashed_key = self._hash_mod(key) 

        if self.storage[hashed_key] != None:
            # loop through the linked list 
            # place the new value in the next linkedList if it is None 
            # else continue to iterate through the linked list.

            current_node = self.storage[hashed_key] 

            while current_node.next != None:
                current_node = current_node.next

            current_node.next = LinkedPair(key, value)
        else:
            self.storage[hashed_key] = LinkedPair(key, value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # first create a variable that holds the hashed_key 
        # create a variable that holds the current node self.storage[hashed_key]
        # create a variable that holds the past node 

        # loop through the linked list 
            # if key equals current_node.key:
                # modify previous_node.next to read current_node.next
                # modify current_node to read None
            # else modify past_node to current_node modify current_node to next node 
        hashed_key = self._hash_mod(key) 
        current_node = self.storage[hashed_key]
        past_node = None

        while current_node:
            if current_node.key == key:
                if current_node.next != None:
                    past_node.next = current_node.next 
                    break
                if current_node.next == None and past_node == None:
                    self.storage[hashed_key] = None
                    break
                else:
                    past_node.next = None 
                    break
            
            else:
                past_node = current_node 
                current_node = current_node.next
        
        print('Invalid key input')
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # basic plan:
        # hash the key and place it in a new variable
        # create a new variable that has the head node as the current_node 
        # loop through the linked list until current_node has the same key 
        # return the value through current_node.value 

        hashed_key = self._hash_mod(key) 
        current_node = self.storage[hashed_key] 

        while current_node:
            if current_node.key == key:
                return current_node.value
            
            current_node = current_node.next
        
        return None 


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass

## testing out the hashing function.
# it seems that they are using the built in hash function in self._hash()
# and using the self._mod_hash() divide the resulting hash value by 
# self.capacity through modulo operator.

new_table = HashTable(2) 
print(new_table._hash_mod('me_1'))
print(new_table._hash_mod('me_2'))
print(new_table._hash_mod('me_3'))
print(new_table._hash_mod('me_4'))
print(new_table._hash_mod('me_5'))
# interesting the created index is different everytime the code is ran. I hope this 
# doesn't cause problems.

# new_table.insert('me_1', 'new_value') 
# new_table.insert('me_2', 'second_value')
# new_table.insert('me_3', 'third_value')
# new_table.insert('me_4', 'fourth_value')
# new_table.insert('me_5', 'fifth_value')
# print(new_table.retrieve('me_1'))
# new_table.remove('me_4')
# print(new_table.retrieve('me_1'))
# print(new_table.retrieve('me_2'))
# print(new_table.retrieve('me_3'))
# print(new_table.retrieve('me_4'))

ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
