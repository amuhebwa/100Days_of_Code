class Solution:
    def mark_boundaries(self, grid, r, c, rows, columns):
        if r < 0 or r == rows or c < 0 or c == columns or grid[r][c] != 1:
            return
        grid[r][c]='*'
        self.mark_boundaries(grid, r+1, c, rows, columns)
        self.mark_boundaries(grid, r-1, c, rows, columns)
        self.mark_boundaries(grid, r, c+1, rows, columns)
        self.mark_boundaries(grid, r, c-1, rows, columns)
        

    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        '''
        Loop through the matrix, and if you encounter the land cell (1) that is on the border,
        do a depth first search and mark it as a no count. This can be done in two ways; 
        (1) mark it with a special character e.g., # or '*' or any unique character
        (2) Add it to the set of visited cells to make sure that we never visit it 
        '''

        ROWS, COLUMNS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1 and (r in [0, ROWS-1] or c in [0, COLUMNS-1]):
                    self.mark_boundaries(grid, r, c, ROWS, COLUMNS)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    islands += 1
        

        return islands