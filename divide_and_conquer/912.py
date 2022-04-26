class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)>1:
            # Finding the mid of the array
            mid = len(nums)//2
            # Dividing the array elements
            l = nums[:mid]
            # into 2 halves
            r = nums[mid:]
            # Sorting the first half
            self.sortArray(l)
            # Sorting the second half
            self.sortArray(r)
            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] =l [i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k += 1
            # Checking if any element was left
            # at this point either l or r is empty
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1
        return nums
        # merge sort https://www.geeksforgeeks.org/merge-sort/