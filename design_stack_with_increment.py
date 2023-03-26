class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.n = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        l = min(len(self.stack), k)
        for i in range(l):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)