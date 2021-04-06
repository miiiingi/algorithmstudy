class newMystack : 
    def __init__(self) -> None:
        self.stack = [] 
    
    def push(self, x) : 
        self.stack.append(x)

    def top(self) : 
        return self.stack[-1]
    
    def pop(self) :
        return self.stack.pop()
    
    def empty(self) : 
        return len(self.stack) == 0 
stack = newMystack()    
stack.push(1)
stack.push(2)
stack.top()
stack.pop()
stack.empty()
