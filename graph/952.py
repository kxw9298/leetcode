class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        mn = max(nums)
        N = len(nums)
        m = list(range(mn+1))
        
        for n in nums:
            for k in range(2, int(math.sqrt(n))+1):
                if n % k == 0:
                    self.u(m, n, k)
                    self.u(m, n, n // k)
        count = collections.defaultdict(int)
        for n in nums:
            count[self.f(m,n)] += 1
        return max(count.values())
    
    def f(self, m, n):
        while m[n] != n:
            m[n] = m[m[n]]
            n = m[n]
        return n
        
    def u(self, m, a, b):
        if m[a] == m[b]: return
        pa = self.f(m, a)
        pb = self.f(m, b)
        m[pa] = pb

# https://blog.csdn.net/fuxuemingzhu/article/details/85015411