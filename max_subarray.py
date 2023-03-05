class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if len(nums) == 0:
        #    return 0
        # better solution: credit: neetcode
        cur_Sum, max_sum = 0, nums[0]
        for  n in nums:
            if cur_Sum < 0:
                cur_Sum = 0
            cur_Sum +=  n
            max_sum = max(max_sum, cur_Sum)
        return max_sum