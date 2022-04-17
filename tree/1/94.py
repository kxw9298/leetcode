# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :rtype List[int]
        """
        answer = []
        stack = []
        # curr = root;   
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            answer.append(root.val)
            root = root.right
        
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if not stack:
        #         return answer
        #     root = stack.pop()
        #     answer.append(root.val)
        #     root = root.right
                
        
        # self.inorder(root, answer)
        return answer
    # recursive
    def inorder(self, root: Optional[TreeNode], answer: List[int]):
            # if root == None:
            #     return None
            # if root.left != None:
            #     self.inorder(root.left, answer)
            # answer.append(root.val)
            # if root.right != None:
            #     self.inorder(root.right, answer)
            if root != None:
                self.inorder(root.left, answer)
                answer.append(root.val)
                self.inorder(root.right, answer)