"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        # for child in root.children:
        #     res.extend(self.postorder(child))
        # res.append(root.val)
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return reversed(res)