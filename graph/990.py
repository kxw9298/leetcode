class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        for eq in equations:
            if eq[1] == '=':
                dsu.union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))
        for eq in equations:
            if eq[1] == '!':
                if dsu.find(ord(eq[0]) - ord('a')) == dsu.find(ord(eq[3]) - ord('a')):
                    return False
        return True
        
class DSU:
    def __init__(self):
        self.m = list(range(26))
    def find(self, x):
        if self.m[x] != x:
            self.m[x] = self.find(self.m[x])
        return self.m[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.m[px] = py

# https://blog.csdn.net/fuxuemingzhu/article/details/87862736