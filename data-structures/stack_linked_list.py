# Stack implementation using linked list

class Node:
  def __init__(self,value):
      self.value = value
      self.next = None

class Stack:    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    # TODO: Add the push method
    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node