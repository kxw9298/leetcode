class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        queue = collections.deque()
        graph = collections.defaultdict(set)
        routes = list(map(set, routes))
        seen, targets = set(), set()
        for i in range(len(routes)):
            if source in routes[i]: # possible starting route number
                seen.add(i)
                queue.append((i,1))
            if target in routes[i]: # possible ending route number
                targets.add(i)
            for j in range(i+1, len(routes)):
                if routes[j] & routes[i]: # set intersection to check if route_i and route_j are connected
                    graph[i].add(j)
                    graph[j].add(i)
        while queue:
            cur, count = queue.popleft()
            if cur in targets:
                return count
            for neighbour in graph[cur]:
                if neighbour not in seen:
                    queue.append((neighbour, count + 1))
                    seen.add(neighbour)
        return -1

# https://leetcode.com/problems/bus-routes/solution/