It was unclear from the problem scope if a member of a sub-group returned true when it's parent group was searched. 
This solution does not do that.

Recursive helper function makes use of converting lists to sets to improve search time 
(O(n) to O(1)). 

Time complexity\
return_is_user_in_group(): O(m) - O(1) user in set(group.get_users()) and m groups per level\
LRUCache.set_head(): O(1) - Hash Map operation, list append, no cache traversal necessary\

Space complexity\
LRUCache.set(): O(1) - Cache size fixed.\
LRUCache.set_head(): O(1) - Because the cache size is fixed, rehashing wasn't needed to expand the bucket array\
LRUCache.get(): O(1) - The compressions kept the outputs to a single integer. 