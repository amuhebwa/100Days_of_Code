class Solution:
    def binsearch(self, arr, target):
        n = len(arr)
        low, high, first_pos = 0, n-1, n 
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] >= target:
                first_pos = mid
                high = mid - 1
            else:
                low = mid + 1
        return first_pos
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first_occ = self.binsearch(nums, target)
        last_occ = self.binsearch(nums, target+1) - 1
        if first_occ <= last_occ:
            return [first_occ, last_occ]
        return [-1, -1]
        