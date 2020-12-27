class Stack:
    def __init__(self, initial_size = 10):
        # initialize with array of size 10 - 0s represent 'empty' slots
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0