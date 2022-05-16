class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        mn = max(nums)
        N = len(nums)
        self.p = list(range(mn+1))
        
        for n in nums:
            for k in range(2, int(math.sqrt(n))+1):
                if n % k == 0:
                    self.u(n, k)
                    self.u(n, n // k)
        count = collections.defaultdict(int)
        for n in nums:
            count[self.f(n)] += 1
        return max(count.values())
    
    def f(self,n):
        while self.p[n] != n:
            self.p[n] = self.p[self.p[n]]
            n = self.p[n]
        return n
        
    def u(self, a, b):
        if self.p[a] == self.p[b]: return
        pa = self.f(a)
        pb = self.f(b)
        self.p[pa] = pb

# https://blog.csdn.net/fuxuemingzhu/article/details/85015411