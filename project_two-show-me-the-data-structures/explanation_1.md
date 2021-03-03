## Approach
This solution uses Python's ordered dictionary data structure to allow for (1) efficient lookups in constant time (O(1)) and (2) for finding and removing the least recently used item in constant time, using the popitem() method. 

## Time Complexity
Get() and set() operation for this solution have a time complexity of O(1).

## Space Complexity
The space requirements will grow linearly with the size of the input: the more items there are to store, the more space the dictionary will take up. So the space complexity is O(n).

