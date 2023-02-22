class Solution:
    def fill_neighbors(self, image, r, c, ROWS, COLUMNS, curr_color, new_color):
        if r < 0 or r == ROWS or c < 0 or c == COLUMNS or image[r][c] != curr_color:
            return
        image[r][c] = new_color
        self.fill_neighbors(image, r-1, c, ROWS, COLUMNS, curr_color, new_color)
        self.fill_neighbors(image, r+1, c, ROWS, COLUMNS, curr_color, new_color)
        self.fill_neighbors(image, r, c-1, ROWS, COLUMNS, curr_color, new_color)
        self.fill_neighbors(image, r, c+1, ROWS, COLUMNS, curr_color, new_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        ROWS, COLUMNS = len(image), len(image[0])
        curr_color = image[sr][sc]
        self.fill_neighbors(image, sr, sc, ROWS, COLUMNS, curr_color, color)
        return image