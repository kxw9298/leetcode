class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
    
    def dfs(self, rooms, index, visited):
        visited.add(index)
        for n in rooms[index]:
            if n not in visited:
                self.dfs(rooms, n, visited)