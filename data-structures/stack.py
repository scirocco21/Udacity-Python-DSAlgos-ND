class Stack:
    def __init__(self, initial_size = 10):
        # initialize with array of size 10 - 0s represent 'empty' slots
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    
    def push(self, value):
        # use next_index property to insert at top of the stack
        self.arr[next_index] = value
        # increment next_index and num_elements
        self.next_index += 1
        self.num_elements += 1