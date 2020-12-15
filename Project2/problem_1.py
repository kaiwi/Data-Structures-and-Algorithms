# LRU Cache

# LRU_Cache class
class LRU_Cache(object):
    def __init__(self, capacity=5, initial_size=8):  # Bucket size set to minimum size to achieve < 0.7 load factor
        # Initialize class variables
        self.capacity = capacity
        self.current_cache_size = 0

        # Use a DoublyLinkedList data structure to simulate CacheNodes moving based on new set() keys
        self.head = None
        self.tail = None

        # Use a hash map  data structure to aid in O(1) get() & set()
        self.bucket_array = [CacheNode() for _ in range(initial_size)]
        self.p = 31

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.get(key) == -1:  # Key not in cache
            if self.current_cache_size == 5:  # Full cache
                #print("^^^FULL CACHE^^^")
                new_tail = self.tail.previous
                self.tail.previous = None  # Remove old tail
                self.bucket_array[self.get_bucket_index(self.tail.key)] = CacheNode()  # Vacate the bucket array at bucket index
                self.tail = new_tail  # Set new tail
                self.tail.next = None
                self.current_cache_size -= 1  # Update cache_size
                self.set_head(key, value)  # Set new head

            else:  # Space available in cache
                self.set_head(key, value)  # Set new head
        else:  # Key is in cache
            node = self.head  # Search for key in cache starting at cache head
            while node:
                if node.key == key:
                    if not node.previous:  # If key at head
                        break  # Do nothing
                    # if not node.previous and node.key == key:
                    #     return
                    elif not node.next:  # If key at tail
                        self.tail = node.previous  # Set previous to tail
                        node.previous.next = None  # Remove tail
                    # elif not node.next and node.key == key:
                    else:  # If key in middle
                        node.previous.next = node.next  # Attach previous to next node
                        node.next.previous = node.previous  # Attach next to previous
                    node.previous = None  # Establish new head
                    node.next = self.head
                    self.head.previous = node
                    self.head = node
                    break
                node = node.next  # Step through cache
        return

    def set_head(self, key, value):
        # Sets a new LRU Cache head.
        #print("SETTING NEW HEAD")
        new_node = CacheNode(key, value)
        #print("new_node:\n{}".format(new_node))
        bucket_index = self.get_bucket_index(key)  # Assign bucket index for new CacheNode
        self.bucket_array[bucket_index] = new_node  # Store new CacheNode in bucket_array at bucket_index
        #print("bucket_array[{}]:\n{}".format(bucket_index, self.bucket_array[bucket_index]))
        if self.head:  # Cache is not empty
            old_head = self.head
            #print("old_head:\n{}".format(old_head))
            new_node.next = old_head  # Point new_node to old_head
            old_head.previous = new_node  # Point old_head to new_head
            #print("new_node:\n{}".format(new_node))
        else:  # Cache is empty
            self.tail = new_node
        self.head = new_node  # Update head
        self.current_cache_size += 1  # Increment current_cache_size
        # print("set_head LRU_Cache:\n", self.__repr__()
        return

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        bucket_index = self.get_bucket_index(key)
        #print("bucket_index: ", bucket_index)
        if self.current_cache_size == 0:  # Empty cache
            return -1
        node = self.bucket_array[bucket_index]  # Grab CacheNode at bucket_index; O(1)
        #print("GET NODE: {}".format(node))
        if node.key == key:
            #print("*-\CACHE HIT/-*")
            print(node.value)
            return node.value  # Cache hit
        #print("*-/CACHE MISS\-*")
        print(-1)
        return -1  # Cache miss

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient

        return hash_code % num_buckets  # one last compression before returning

    def __repr__(self):
        s = "**********************************\n"
        s += "**********  LRU Cache  ***********\n"
        s += "**********************************\n"
        s += "capacity: {} | current cache size: {}\n"
        s += "**********************************\n"

        node = self.head
        while node:
            if node.previous == None:  # head
                s += "HEAD\n{}\n".format(node)
            elif node.next == None: # tail
                s += "TAIL\n{}\n".format(node)
            else:
                s += "{}\n".format(node)

            node = node.next
        return s.format(self.capacity,
                        self.current_cache_size,
                        self.head,
                        self.tail,
                        )

# CacheNode class
class CacheNode(object):
    # CacheNodes combine Hash Maps [to achieve O(1) set() & get()] and doubly linked lists
    # [to simulate LRU movement]
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        s = "[key: {} | value: {}]\n".format(self.key, self.value)
        if self.previous and self.next:
            s += "[previous: {} | next: {}]\n".format(self.previous.key, self.next.key)
        elif self.previous and not self.next:
            s += "[previous: {} | next: {}]\n".format(self.previous.key, self.next)
        elif self.next and not self.previous:
            s += "[previous: {} | next: {}]\n".format(self.previous, self.next.key)
        elif not self.next and not self.previous:
            s += "[previous: {} | next: {}]\n".format(self.previous, self.next)

        return s

def print_bucket_array(cache):
    #Prints the bucket array for a LRU cache
    for index,value in enumerate(cache.bucket_array):
        print("Index[{}]\n{}".format(index,value))
    return

#Test Cases
our_cache = LRU_Cache()
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(4, 4)
our_cache.set(2, 2)
our_cache.set(5, 5)
our_cache.set(11, 11)
our_cache.set(13, 13)
print_bucket_array(our_cache)
print(our_cache)
#
#
our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache
#
#
our_cache.get(6)      # returns -1 because the cache reached it's capacity and 6 was the least recently used entry
