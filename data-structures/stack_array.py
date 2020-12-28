# stack implementation using array
class Stack:
    def __init__(self, initial_size = 10):
        # initialize with array of size 10 - 0s represent 'empty' slots
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    
    def push(self, value):
        if len(self.arr) == self.next_index:
          self.handle_stack_capacity_full()
        # use next_index property to insert at top of the stack
        self.arr[self.next_index] = value
        # increment next_index and num_elements
        self.next_index += 1
        self.num_elements += 1
      
    def handle_stack_capacity_full(self):
        # copy over old array
        old_arr = self.arr
        # create new array with larger size
        self.arr = [0 for i in range(2*len(old_arr))]
        # write old array values into new array at same positions
        for index,value in enumerate(old_arr):
            self.arr[index] = value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
    
    def pop(self):
        if self.is_empty():
          return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]