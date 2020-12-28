# Stack implementation using linked list

class Node:
  def __init__(self,value):
      self.value = value
      self.next = None

class Stack:    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node

        self.num_elements += 1
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.head is None:
            return None
        top = self.head
        self.head = top.next
        self.num_elements -= 1
        return top