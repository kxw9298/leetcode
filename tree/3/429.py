"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        # queue = collections.deque()
        # queue.append(root)
        # while queue:
        #     level = []
        #     # the length of current level
        #     size = len(queue)
        #     for _ in range(size):
        #         node = queue.popleft()
        #         if not node:
        #             continue
        #         level.append(node.val)
        #         for child in node.children:
        #             queue.append(child)
        #     if level:
        #         res.append(level)
        self.getLevel(root, res, 0)
        return res
    
    def getLevel(self, root, res, level):
        if not root:
            return
        while len(res) <= level:
            res.append([])
        res[level].append(root.val)
        for child in root.children:
            self.getLevel(child, res, level + 1)
       
            
        return res