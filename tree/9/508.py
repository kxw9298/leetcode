# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        vals = []
        def getSum(root):
            if not root: return 0
            s = getSum(root.left) + root.val + getSum(root.right)
            vals.append(s)
            return s
        getSum(root)
        count = collections.Counter(vals)
        frequent = max(count.values())
        res = []
        for k, v in count.items():
            if v == frequent:
                res.append(k)
        return res
        # return [x for x, v in count.items() if v == frequent]