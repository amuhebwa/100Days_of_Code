class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) <= 1:
            return False
        _table = {')':'(', ']' : '[', '}' : '{'}
        _stack = []

        for _, val in enumerate(s):
            if val in _table.values():
                _stack.append(val)
            elif len(_stack) != 0 and _table.get(val) == _stack[-1]: # peep
                _stack.pop()
            else:
                return False
        return len(_stack) == 0


            



 