class Solution:
    def set_rows_cols(self, matrix, r, c, ROWS, COLUMNS, already_set):
        already_set.add((r, c))
        for _r in range(r, ROWS):
            if (_r, c) not in already_set:
                matrix[_r][c] = 0
                already_set.add((_r, c))
        for _c in range(c, COLUMNS):
            if (r, _c) not in already_set:
                matrix[r][_c] = 0
                already_set.add((r, _c))
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        rows_to_set, cols_to_set = set(), set()
        for r in range(ROWS):
            for c in range(COLUMNS):
                if matrix[r][c] == 0:
                    rows_to_set.add(r)
                    cols_to_set.add(c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if r in rows_to_set or c in cols_to_set:
                    matrix[r][c] = 0

        #print('rows', rows_to_set)
        #print('cols', cols_to_set)