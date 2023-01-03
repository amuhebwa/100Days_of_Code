class Solution:
    def helper_fn(self, first, second, math_sign):
        result = None
        if math_sign == "+":
            result = first + second
        elif math_sign == '-':
            result = first - second
        elif math_sign == "*":
            result = first * second
        elif math_sign == "/":
            result = first/second
        else:
            pass
        return result
    
    def evalRPN(self, tokens: List[str]) -> int:
        valid_opts = ['+', '-', '*', '/']
        temp_stack = []
        for val in tokens:
            if val not in valid_opts:
                temp_stack.append(val)
            else:
                second = int(temp_stack.pop())
                first = int(temp_stack.pop())
                result = self.helper_fn(first, second, val)
                temp_stack.append(result)
        
        result = None
        if temp_stack:
            result = int(temp_stack.pop())
        return result