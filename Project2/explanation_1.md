I used two classes to implement the solution. The LRUCache used both a linked list and a Hash Map to model LRU cache behavior. The double linked list allowed nodes to reorder 
themselves  and to be able to model the LRU/MRU behaviors. The Hash Map allowed 
for faster cache searches when calling get() to be able to rearrange the cache. The CacheNode 
used a Doubly Linked List data structure to facilitate reordering nodes during cache hits as well as 
functioning properly with the LRUCache class (i.e. head/tail behavior).

Time complexity\
LRUCache.set(): O(m) - m: cache size, traversal necessary for MRU\
LRUCache.set_head(): O(1) - Hash Map operation, list append, no cache traversal necessary\
LRUCache.get(): O(1) - Hash Map operation, list return\

Space complexity\
LRUCache.set(): O(1) - Cache size fixed.\
LRUCache.set_head(): O(1) - Because the cache size is fixed, rehashing wasn't needed to expand the bucket array\
LRUCache.get(): O(1) - The compressions kept the outputs to a single integer. 