# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(l: int, r: int) -> TreeNode:
            if l > r: return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = buildBST(l, m - 1)
            root.right = buildBST(m + 1, r)
            return root
        return buildBST(0, len(nums) - 1)