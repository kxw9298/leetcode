class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, curr, n):
            for i in range(n):
                if M[curr][i] == 1:
                    M[curr][i] = M[i][curr] = 0
                    dfs(M, i, n)
        n = len(isConnected)
        ans = 0
        for i in range(n):
            if isConnected[i][i] == 1:
                ans +=1
                dfs(isConnected, i, n)
        return ans