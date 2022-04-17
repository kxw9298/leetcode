"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        # self.helper(root, res)
        if not root:
            return res;
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(reversed(node.children))
        return res
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        for child in root.children:
            self.helper(child, res)