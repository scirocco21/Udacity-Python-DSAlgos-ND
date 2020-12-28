 """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    brackets = Stack()
    for bracket in list(equation):
        if bracket == "(":
            brackets.push(bracket)
        elif bracket == ")" and brackets.size() > 0:
            brackets.pop()
        elif bracket == ")" and brackets.size() == 0:
            return False
    return brackets.size == 0
        