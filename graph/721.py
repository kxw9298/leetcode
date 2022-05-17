class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_index = {}
        for i in range(n):
            m = len(accounts[i])
            for j in range(1,m):
                email = accounts[i][j]
                if email not in email_to_index:
                    email_to_index[email] = i
                # 存在重复的邮箱地址时，合并
                else:
                    uf.union(i, email_to_index[email])
        # 上面的操作根据邮箱地址将属于同个账户进行合并
        # 现在将合并后的账户对应的所有邮箱地址放到一个列表中
        index_to_email = collections.defaultdict(list)
        for email, index in email_to_index.items():
            index_to_email[uf.find(index)].append(email)
            
        ans = []
        # 根据格式进行合并返回
        for index, email in index_to_email.items():
            ans.append([accounts[index][0]]+sorted(email))
        return ans
                    
        
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py
# https://leetcode.cn/problems/accounts-merge/solution/721-zhang-hu-he-bing-bing-cha-ji-python-3u5nr/