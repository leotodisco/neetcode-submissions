class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val = image[sr][sc]
        COLS = len(image[0])
        ROWS = len(image)
        if image[sr][sc] == color:
            return image

        def dfs(row, col, val):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or image[row][col] != val:
                print("ci sono")
                return
            else:
                image[row][col] = color
                
                dfs(row+1, col, val)
                dfs(row-1, col, val)

                dfs(row, col+1, val)
                dfs(row, col-1, val)
            return

        
        dfs(sr, sc, val)
        return image