### Exercise: Implement a doubly linked list that can append to the tail in constant time. Make sure to include forward and backward connections when adding a new node to the list.
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        # if there's no node, set head and tail values
        if self.head = None:
            self.head = Node(value)
            self.tail = self.head
            return
        # the new node is the one after the (old) tail
        self.tail.next = DoubleNode(value)
        # the new node's previous node is the (old) tail
        self.tail.next.previous = self.tail
        # finally update the tail property
        self.tail = self.tail.next
        