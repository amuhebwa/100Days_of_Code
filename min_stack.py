class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        '''
        if self.min_stack:
            peek = self.min_stack[-1]
            if val <= peek:
                self.min_stack.append(val)
        '''
        '''
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        '''
        '''
        credit to Neetcode for this nice hint: https://youtu.be/qkLl7nAwDPo
        '''
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()
        '''
        self.stack.pop()
        self.min_stack.pop()
        '''

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()