# LRU Cache
from collections import OrderedDict


class LRUCache(OrderedDict):
    """
    Class objects model a Least Recently Used(LRU) cache with limited capacity as an OrderDict subclass.
    FIFO when capacity is exceeded.
    """

    def __init__(self, capacity=5):
        """
        Constructor for LRU.
        :param capacity: Initial size of LRUCache.
        """
        self.capacity = capacity

    def get(self, key):
        """
        Return object at key.
        :param key: Unique integer ID.
        :param value: Integer
        :return: None
        """
        if key not in self.keys():  # cache miss
            return -1
        else:  # cache hit
            self.move_to_end(key)  # move key to head of cache
            return self[key]

    def set(self, key, value):
        """
        Sets the value at key of the LRU if the key is not present. If key is present, If the cache is at capacity,
        removes the oldest item.
        :param key: Unique integer ID.
        :param value: Object to store at key.
        :return: None
        """
        if key is None:
            return
        if self.get(key) == -1:  # key not in cache
            self[key] = value
            if len(self) > self.capacity:
                self.popitem(last=False)  # FIFO
        self.move_to_end(key)  # move key to head of cache


if __name__ == "__main__":
    cache = LRUCache()
    cache.set(1, 1)
    print(cache)  # verify set(), expect [1]
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    cache.set(5, 5)
    print(cache)  # verify FIFO, expect [1, 2, 3, 4, 5]
    cache.set(1, 1)
    print(cache)  # verify LRU behavior, expect: [2, 3, 4, 5, 1]
    cache.set(6, 6)
    print(cache)  # exceed capacity, expect: [3, 4, 5, 1, 6]
    print(cache.get(3))  # verify get(), expect: 3
    print(cache.get(7))  # verify get(), expect: -1
    cache.set(-1, -1)  # verify negative keys
    print(cache)  # expect: [5, 1, 6, 3, -1]
    cache.set(None, 'None')  # verify None input
    print(cache)  # expect: [5, 1, 6, 3, -1]
    cache.set('a', 'a')  # verify string input
    print(cache)  # expect: [1, 6, 3, -1, 'a']

    our_cache = LRUCache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache)
    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9)) # returns -1
    print(our_cache)
    our_cache.set(5, 5)
    print(our_cache)
    our_cache.set(6, 6)
    print(our_cache)
    print(our_cache.get(3))  # returns -1 because key 3 was thrown out
    our_cache.set(7, 7)
    print(our_cache)
    print(our_cache.get(4)) # 4 is thrown out
