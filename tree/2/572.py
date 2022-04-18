# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        # recursive
        # 1 same tree, or 2 sub tree of left chiled or 3 subtree of right child
        # return self.isSameTree(root, subRoot) or \
        #        self.isSubtree(root.left, subRoot) or \
        #        self.isSubtree(root.right, subRoot)
        
        # bfs
        que = collections.deque()
        que.append(root)
        while que:
            node = que.popleft()
            if not node: continue
            if self.isSameTree(node, subRoot): return True
            que.append(node.left)
            que.append(node.right)
        return False
    
    def isSameTree(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False;
        return l.val == r.val and \
               self.isSameTree(l.left, r.left) and \
               self.isSameTree(l.right, r.right)