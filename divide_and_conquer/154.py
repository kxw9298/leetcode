class Solution:
    def findMin(self, nums: List[int]) -> int:
        def _findMin(nums, l, r):
            # 1 or 2 elements
            if l + 1 >= r: return min(nums[l], nums[r])
            # Sorted, must be less than
            if nums[l] < nums[r]: return nums[l]
            m = l + (r - l)//2
            # Recursively find the solution
            return min(_findMin(nums, l, m -1), _findMin(nums, m, r))
        return _findMin(nums, 0, len(nums) - 1)