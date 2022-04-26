class Solution:
    def findMin(self, nums: List[int]) -> int:
        def _findMin(nums, l, r):
            # only 1 or 2 elements
            if l + 1 >= r: return min(nums[l], nums[r])
            
            # Sorted
            if nums[l] < nums[r]: return nums[l]
            
            mid = l + (r-l)//2
            
            return min(_findMin(nums, l, mid - 1), _findMin(nums, mid, r))
        return _findMin(nums, 0, len(nums) - 1)