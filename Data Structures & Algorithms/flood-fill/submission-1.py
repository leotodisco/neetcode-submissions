class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROWS = len(image)
        COLS = len(image[0])
        
        def dfs(row, col, val):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or image[row][col] != val:
                return
            image[row][col] = color
            dfs(row, col+1, val)
            dfs(row, col-1, val)

            dfs(row-1, col, val)
            dfs(row+1, col, val)

            return
        dfs(sr, sc, image[sr][sc])
        return image
