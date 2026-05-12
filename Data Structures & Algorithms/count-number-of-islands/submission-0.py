class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        island=0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=columns or grid[r][c]=="0":
                return 
            grid[r][c]="0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
            
            

        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1":
                    dfs(r,c)
                    island +=1
                        
        return island
        