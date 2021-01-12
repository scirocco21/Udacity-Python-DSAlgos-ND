"""
  Determine whether the Linked List is circular or no
  Args:
      linked_list(obj): Linked List to be checked
  Returns:
      bool: Return True if the linked list is circular, return False otherwise
"""

# SETUP
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

# MAIN FUNCTION
def iscircular(linked_list):
    """
    Idea: initalize fast and slow pointers. 
    In a linked list with a loop, the slow and fast pointer will eventually point to the same node
    If the fast pointer can reach the end of the list, the list can't have a loop
    """
    if linked_list.head is None:
        return False
    slow = linked_list.head
    fast = linked_list.head
    # in the while loop, check that there is a node available 
    # before trying to reference its .next property 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False