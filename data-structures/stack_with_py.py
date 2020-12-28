# implement simple stack with python methods (assume beginning of list == bottom of stack)
class Stack:
    def __init__(self):
        self.arr = []
        
    def size(self):
        return len(self.arr)
    
    def push(self, item):
        self.arr.append(item)
        return self
        
    def pop(self):
        if len(self.arr) == 0:
            return None
        return self.arr.pop()