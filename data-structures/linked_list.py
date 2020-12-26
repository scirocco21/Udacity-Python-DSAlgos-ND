class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
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
    
    def to_list(self):
        node = self.head
        result = []
        while node:
            result.append(node.value)
            node = node.next
        return result

    def prepend(self, value):
        # if there's not a head node already, create one
        if self.head is None:
            self.head = Node(value)
            return
        # otherwise create head one and assign old one to its next property
        node = self.head
        self.head = Node(value)
        self.head.next = node
        return

    def size(self):
      size = 0
      if self.head is None:
          return size
      node = self.head
      while node:
          size += 1
          node= node.next
      return size