class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr_sum, total = 0, 0
        for _, num in enumerate(nums):
            curr_sum += num
            total = min(total, curr_sum)
        return -total + 1