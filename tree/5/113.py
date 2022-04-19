# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        # self.dfs(root, targetSum, res, [])
        que = deque()
        que.append((root, [], 0)) # 将要处理的节点，路径，路径和
        while que:
            node, path, pathSum = que.popleft()
            if not node: # 如果是空节点，不处理
                continue
            if not node.left and not node.right: # 如果是叶子节点
                if node.val + pathSum == targetSum: # 加上叶子节点后，路径和等于sum
                    res.append(path + [node.val]) # 保存路径
            # 处理左子树
            que.append((node.left, path + [node.val], pathSum + node.val))
            # 处理右子树
            que.append((node.right, path + [node.val], pathSum + node.val))
             
        return res
    def dfs(self, root, targetSum, res, path):
        if not root: # 空节点，不做处理
            return
        if not root.left and not root.right: # 叶子节点
            if targetSum == root.val: # 剩余的「路径和」恰好等于叶子节点值
                res.append(path + [root.val]) # 把该路径放入结果中
        self.dfs(root.left, targetSum - root.val, res, path + [root.val]) # 左子树
        self.dfs(root.right, targetSum - root.val, res, path + [root.val]) # 右子树