to_set() LinkedList method added to convert the LinkedLists to sets to improve intersection time complexity instead of 
traversing both LinkedLists and searching for duplicates (in the output LinkedList). 

Time complexity\
LinkedList.to_set(): O(n) - traverses entire LinkedList\
union(): O(n\*m\*(len(s)+len(t))\*p) - to_set both LinkedLists (n\*m), set.union() and conversion back to LinkedList(p).\
intersection(): O(n\*m\*min(len(m), len(n))\*p) - to_set both LinkedLists (n\*m), set.intersection() and conversion back 
to LinkedList(p).

Space complexity\
LinkedList.to_set(): O(n) - duplicates LinkedList space\
union(): O((n+m)^2) - each LinkedList is duplicated (to_set()) and combines space from both LinkedLists 
(if all elements are unique from both sets)\
intersection(): O((n+m)\*min(len(m), len(n))) - each LinkedList is duplicated (to_set()) and the intersection set 
has to be converted back into a LinkedList.