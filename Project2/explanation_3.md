This problem was particularly challenging since I didn't realize heapq existed until after I failed at implementing my 
own min heap class.

To encode, I used a dictionaries to store the character/frequency/code pairs and used the min heap to sort them into a 
priority queue. To decode, I converted the input data string to a deque for O(1) bit pops.


Time complexity\
huffman_encoding(): O(n^4 log^2 n)\
O(n) char/freq dict creation, O(n^2 log n) heappush (entire dict), O(n) char to code\
in_order(): O(d) - depth of heap dependent\  
huffman_decoding(): O(n) - complete data queue traversal needed to decode


Space complexity\
huffman_encoding(): O(n^3*m)\
char-freq O(n) and char-code O(n) dictionaries and heap O(n) grow linearly with 
character diversity in data. O(m) - len(encoded_data)

