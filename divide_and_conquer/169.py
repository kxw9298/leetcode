class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap
        # count = collections.Counter(nums)
        # return count.most_common(1)[0][0]
        
        # divide and conquer
        # https://jianengli.github.io/2020/12/12/leetcode/sort/169/
        return self.help(0,len(nums)-1,nums)
    
    def help(self,low,high,nums):
        # base case; the only element in an array of size 1 is the majority
        # element.
        if low == high:
            return nums[low]
        
        # recurse on left and right halves of this slice.
        mid = (high-low)//2 + low
        left = self.help(low,mid,nums)
        right = self.help(mid+1,high,nums)

        # if the two halves agree on the majority element, return it.
        if left == right:
            left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(low,high+1) if nums[i]==left)
        right_count = sum(1 for i in range(low,high+1) if nums[i]==right)
        return left if left_count > right_count else right