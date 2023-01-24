class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        _count = 0
        for i in range(rows-1, -1, -1):
            for j in range(columns-1, -1, -1):
                if grid[i][j] < 0:
                    _count += 1
        return _count
