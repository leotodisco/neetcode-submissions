class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(row, col):
            if row<0 or row >= ROWS or col<0 or col>=COLS or grid[row][col]==0:
                return 1
            if (row, col) in visit:
                return 0
            visit.add((row, col))
            perim = dfs(row, col+1) + dfs(row+1, col)+dfs(row, col-1) + dfs(row-1, col)
            return perim
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i, j)
        return 0

        



        