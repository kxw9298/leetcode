class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.island = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    self.dfs(grid, i, j, M, N)
                    self.res = max(self.res, self.island)
                    self.island = 0
        return self.res
    
    def dfs(self, grid, i, j, M, N):
        if i < 0 or j <0 or i >= M or j >= N or grid[i][j] == 0: return
        grid[i][j] = 0
        self.island += 1
        self.dfs(grid, i+1, j, M, N)
        self.dfs(grid, i-1, j, M, N)
        self.dfs(grid, i, j+1, M, N)
        self.dfs(grid, i, j-1, M, N)