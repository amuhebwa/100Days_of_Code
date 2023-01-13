
if __name__=="__main__":

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    ROWS, COLUMNS = len(grid), len(grid[0])
    isvisited = set()
    def dfs(grid, r, c):
        if r < 0 or r == ROWS or c < 0 or c == COLUMNS or (r, c) in isvisited or grid[r][c] == 0:
            return 0
        isvisited.add((r, c))
        return (1 + dfs(grid, r-1, c)+ dfs(grid, r+1, c)+ dfs(grid, r, c-1)+ dfs(grid, r, c+1))
    max_area = 0
    for r in range(ROWS):
        for c in range(COLUMNS):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(grid, r, c))

    print(max_area)







