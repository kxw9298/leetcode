class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        deq = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    deq.append([i,j])
        if not len(deq) or len(deq) == M*N:
            return -1
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)];
        
        distance = -1
        
        while len(deq):
            distance += 1
            
            size = len(deq)
            while size:
                size -= 1
                cur = deq.pop(0)
                for i,j in directions:
                    x = cur[0] + i
                    y = cur[1] + j
                    if x<0 or x>=M or y<0 or y>=N or grid[x][y] != 0:
                        continue
                    grid[x][y] = 2
                    deq.append([x,y])
        
        return distance
#   https://blog.csdn.net/fuxuemingzhu/article/details/105175455         
            
        