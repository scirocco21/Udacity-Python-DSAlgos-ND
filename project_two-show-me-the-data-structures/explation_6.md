
## Time Complexity

- For *union*, the time complexity is determined by the length of the longest linked list, which has to be traversed in full for this solution. 

In other words, the time complexity is O(n), where n = max(linked_list_1.size, linked_list_2.size)

- For *intersection*, the time complexity is again O(n), where n is the length of the longest linked list (if any). This is because the method requires only a single pass over the two lists and will complete its calculations when the end of both lists has been reached.

