class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #color[i], 0 means not visited. 1 means safe. 2 means unsafe.
        color = [0]*len(graph)
        res = []
        for start in range(len(graph)):
            if self.dfs(graph, start, color):
                res.append(start)
        res.sort()
        return res
    def dfs(self, graph, start, color):
        # 返回start节点是否是安全，如果是，返回True
        if color[start] != 0:
            return color[start] == 1
        color[start] = 2
        for e in graph[start]:
            if not self.dfs(graph, e, color):
                return False
        color[start] = 1
        return True

            
        
        