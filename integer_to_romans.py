class Solution:
    def intToRoman(self, num: int) -> str:
        from sortedcontainers import SortedList

        table = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        keys = [*table.keys()]
        values = [*table.values()]
        keys.reverse()
        values.reverse()

        res = ""
        for k, v in zip(keys, values):
            if num // k:
                n = int(num//k)
                res += v*n
                # print(num%k)
                num = num%k
        # print(res)
        return res