class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        areas = []


        def dfs(row, col, grid):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            area=1 

            area+=dfs(row+1, col, grid)
            area+=dfs(row-1, col, grid)
            area+=dfs(row, col+1, grid)
            area+=dfs(row, col-1, grid)
            return area
       

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    areas.append(dfs(i, j, grid))

        return max(areas) if areas else 0
