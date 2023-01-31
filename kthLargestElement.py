class Solution:
    def quickSelect(self, low, high, k, nums):
        i = low
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]

        if i > k:
            return self.quickSelect(low, i-1, k, nums)
        elif i < k:
            return self.quickSelect(i+1, high, k, nums)
        else:
            return nums[i]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        return self.quickSelect(0, len(nums)-1, k, nums)