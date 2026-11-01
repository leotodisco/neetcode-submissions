class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # trova le componenti connesse
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r, c):
            # controllo se il nodo esiste o è stato visitato
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c]=="0":
                return
            # setto a 0 -> visito
            grid[r][c] = "0"

            # esploro i vicini
            # mi fa settare a 0 tutte le celle della componente connessa a 1
            dfs(r+1, c)
            dfs(r-1, c)

            dfs(r, c+1)
            dfs(r, c-1)

            
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    # trova e setta a 0 tutte le celle della componente connessa.
                    dfs(i, j)
                    islands+=1

        return islands
