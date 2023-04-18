class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0]* cols for i in range(rows) ]
        for i in range(rows):
            for j in range(cols):
                # dp[i][j] = grid[i][j]
                dp[i][j] += grid[i][j]
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i][j-1], dp[i-1][j])
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]
                else:
                    pass

        #print(dp)
        #print(f'Rows: {rows} | cols: {cols}')

        return dp[rows-1][cols-1]