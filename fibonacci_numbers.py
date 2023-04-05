class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        res = [0]*(n+1)
        res[0], res[1] = 0, 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
            print(f'index = {i}', res)
        print('-> ', res)
        return res[n]