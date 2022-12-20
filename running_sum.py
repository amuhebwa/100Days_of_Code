class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        i = 0
        for j in range(1, len(nums)):
            nums[j] = nums[i] + nums[j]
            i += 1
        return nums