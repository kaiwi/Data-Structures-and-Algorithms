# LRU Cache

class LRUCache(object):
    """
    Class objects model a Least Recently Used(LRU) cache with limited capacity. When capacity is exceeded, the LRU node
    is removed from the cache.
    """
    def __init__(self, capacity=5, initial_size=8):  # Bucket size set to minimum size to achieve < 0.7 load factor
        """
        Constructor for LRUCache.
        :param capacity: Initial size of LRUCache.
        :param initial_size: Initial size of Hash Map bucket array.
        """
        # Initialize class variables
        self.capacity = capacity
        self.current_cache_size = 0

        # Use a LinkedList data structure to simulate CacheNodes moving based on new set() keys
        self.head = None
        self.tail = None

        # Use a hash map  data structure to aid in O(1) get() & set()
        self.bucket_array = [CacheNode() for _ in range(initial_size)]
        self.p = 31

    def set(self, key, value):
        """
        Sets the CacheNode at the top of the cache if the key is not present in the cache. Otherwise, resorts the cache
        to place the key CacheNode at the top of the cache. If the cache is at capacity, removes the oldest item.
        :param key: Unique integer ID.
        :param value: Integer
        :return: None
        """
        if key is None:  # do nothing if key is None
            return
        if self.get(key) == -1:  # Key not in cache
            if self.current_cache_size == 5:  # Full cache
                new_tail = self.tail.previous
                self.tail.previous = None  # Remove old tail
                self.bucket_array[
                    self.get_bucket_index(self.tail.key)] = CacheNode()  # Vacate the bucket array at bucket index
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
                    elif not node.next:  # If key at tail
                        self.tail = node.previous  # Set previous to tail
                        node.previous.next = None  # Remove tail
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
        """
        Sets a new LRUCache head.
        :param key: Unique integer ID.
        :param value: Integer
        :return: None
        """

        new_node = CacheNode(key, value)
        bucket_index = self.get_bucket_index(key)  # Assign bucket index for new CacheNode
        self.bucket_array[bucket_index] = new_node  # Store new CacheNode in bucket_array at bucket_index

        if self.head:  # Cache is not empty
            old_head = self.head
            new_node.next = old_head  # Point new_node to old_head
            old_head.previous = new_node  # Point old_head to new_head

        else:  # Cache is empty
            self.tail = new_node
        self.head = new_node  # Update head
        self.current_cache_size += 1  # Increment current_cache_size

        return

    def get(self, key):
        """
        Retrieve item from provided key.
        :param key: Unique integer ID.
        :return: Return value of CacheNode at key; -1 if non-existent.
        """

        bucket_index = self.get_bucket_index(key)

        if self.current_cache_size == 0:  # Empty cache
            return -1
        node = self.bucket_array[bucket_index]  # Grab CacheNode at bucket_index; O(1)

        if node.key == key:
            return node.value  # Cache hit
        return -1  # Cache miss

    def get_bucket_index(self, key):
        """
        Passes key to class method get_hash_code. Returns a compressed hash integer to be used as the index for key in
        the Hash Map bucket array.
        :param key: Unique integer ID.
        :return: Integer
        """
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        """
        Generates a compressed hash integer to be used as Hash Map indices.
        :param key: Unique integer ID.
        :return: Integer
        """
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
            elif node.next == None:  # tail
                s += "TAIL\n{}\n".format(node)
            else:
                s += "{}\n".format(node)

            node = node.next
        return s.format(self.capacity,
                        self.current_cache_size,
                        self.head,
                        self.tail,
                        )


class CacheNode(object):
    """
    A CacheNode object combines Hash Maps and doubly linked lists to simulate LRU cache behavior.
    """
    def __init__(self, key=None, value=None):
        """
        Constructor for CacheNode.
        :param key: Unique integer ID.
        :param value: Integer
        """
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
    """
    Prints the bucket array for a LRU cache.
    :param cache: LRUCache
    :return:
    """
    for index, value in enumerate(cache.bucket_array):
        print("Index[{}]\n{}".format(index, value))
    return


if __name__ == "__main__":
    # LRU cache operational test cases
    our_cache = LRUCache()
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)  # to test exceeding cache capacity: expect 6-5-4-3-2, 1 dropped.
    print(our_cache.get(1))  # returns -1 cache capacity reached and 1 was the least recently used entry
    print(our_cache)
    our_cache.set(4, 4)  # to test key in cache being moved to top of cache and cache reordered: expect 4-6-5-3-2
    print(our_cache)

    #  LRU cache input test cases
    new_cache = LRUCache()
    new_cache.set(-1, 25)  # negative input
    new_cache.set(None, 25)  # no input
    new_cache.set('a', 25)  # string input
    print(new_cache)



