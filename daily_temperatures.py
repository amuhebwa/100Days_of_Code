class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        good solution: credit to neetcode
        """
        '''
        for i in range(0, len(temperatures)):
            cnt = 0
            for j in range(i, n):
                if temperatures[i] <= temperatures[j]:
                    cnt += 1
                else:
                    cnt = 0
            res[i] = cnt
            cnt = 0
        print(res)
        '''
        wait_days, res = [], [i*0 for i in range(0, len(temperatures))]
        n = len(temperatures) - 1
        for i in range(n, -1, -1):
            while wait_days and temperatures[i] >= wait_days[-1][1]:
                wait_days.pop()
            if wait_days:
                res[i] = wait_days[-1][0] - i
            wait_days.append((i, temperatures[i]))
        return res