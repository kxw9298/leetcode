class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        graph = [[] for i in range(n)]
        for path in paths:
            graph[path[0] - 1].append(path[1] - 1)
            graph[path[1] - 1].append(path[0] - 1)
        for i in range(n):
            neighbor_colors = []
            for neighbor in graph[i]:
                neighbor_colors.append(res[neighbor])
            for color in range(1,5):
                if color in neighbor_colors: continue
                res[i] = color
                break
        return res
# https://blog.csdn.net/fuxuemingzhu/article/details/91357466