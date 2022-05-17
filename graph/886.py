class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]-1].append(dislike[1]-1)
            graph[dislike[1]-1].append(dislike[0]-1)
        color = [0]*n
        for i in range(n):
            if color[i] !=0: continue
            q = collections.deque()
            q.append(i)
            color[i] = 1
            while q:
                cur = q.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        q.append(e)
        return True
# https://blog.csdn.net/fuxuemingzhu/article/details/82827177