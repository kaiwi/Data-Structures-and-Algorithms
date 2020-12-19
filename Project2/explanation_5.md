Two data structures were used to produce the solution: a Hash Map hash key, and two
separate Linked Lists (one for the Blockchain, another to handle Block Hash Map collisions). 

Time complexity\
Blockchain.set(): O(1) - unless rehash needed (see _rehash())\
Blockchain.get(): O(m) - m possible separate chain lins to traverse\
Blockchain._rehash(): O(n\*m) - n buckets in original bucket array with m possible separate chain
links to traverse\

Space complexity\
Blockchain.set():O(1)\
Blockchain.get():O(1)\
Blockchain._rehash(): O(2n) - bucket array doubles in space\
