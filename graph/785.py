class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 0-not visited; 1-blue; 2-red;
        visited = [0]*len(graph) 
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft() #every point
                    for e in graph[v]: #every edge
                        if visited[e] !=0:
                            if visited[e] == visited[v]:
                                return False
                        else:
                            visited[e] = 3 - visited[v]
                            q.append(e)
        return True
        