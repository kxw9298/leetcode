# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # DFS
        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        # BFS
        que = collections.deque()
        que.append(target.val)
        visited = set([target.val])
        for _ in range(k):
            size = len(que)
            for i in range(size):
                node = que.popleft()
                for j in conn[node]:
                    if j not in visited:
                        que.append(j)
                        visited.add(j)
        return list(que)
# https://blog.csdn.net/fuxuemingzhu/article/details/82709619