class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ct = [0] * (n+1)
        for x, y in trust:
            ct[x] -=1
            ct[y] += 1
        for i in range(1, n+1):
            if ct[i] == n-1:
                return i
        return -1
# https://maxming0.github.io/2020/05/10/Find-the-Town-Judge/