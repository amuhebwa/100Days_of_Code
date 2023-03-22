class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        credit to nick White for a solid explanation
        https://youtu.be/97oTiOCuxho
        '''
        if not nums or len(nums) < 1:
            return 0
        left = 0
        max_cnt = 0
        for i, val in enumerate(nums):
            k -= (1-val)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            else:
                max_cnt = max(max_cnt, (i-left) + 1)
        return max_cnt