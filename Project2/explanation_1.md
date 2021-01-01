I implemented my class as an object of the OrderedDict subclass. This allowed for FIFO implementation as well as O(1) 
operation time complexity.

Time complexity\
LRUCache.set(): O(1) - dictionary set **[]**, OrderedDict.popitem(), and OrderedDict.move_to_end() are O(1)\
LRUCache.get(): O(1) - **in** is O(1)

Space complexity\
LRUCache.set(): O(2) - Method only interacts with a single key/value.\
LRUCache.get(): O(1) - Method only interacts with a single key. 