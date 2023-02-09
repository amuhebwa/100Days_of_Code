class Solution:
    def bad_region(self,r, c, board, rows, columns):
        if r < 0 or r == rows or c < 0 or c == columns or board[r][c] != 'O':
            return
        board[r][c] = "#"
        self.bad_region(r-1, c, board, rows, columns)
        self.bad_region(r+1, c, board, rows, columns)
        self.bad_region(r, c+1, board, rows, columns)
        self.bad_region(r, c-1, board, rows, columns)



    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns = len(board), len(board[0])
        for r in range(rows):
            for c in range(columns):
                # make sure that we are only flagging boarder regions ie those not surrounded
                # by 'X' on all the four corners
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, columns-1]):
                    self.bad_region(r, c, board, rows, columns)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == '#':
                    board[r][c] = 'O'

        print(board)