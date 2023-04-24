class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        kept on timing out
        credit for a work around: https://www.youtube.com/watch?v=qBr2hq4daWE&ab_channel=NickWhite
        '''
        nums.sort()
        _closest, n = float('inf'), len(nums)-1
        for i in range(len(nums)-2):
            left, right = i+1, n
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if abs(_sum - target) < abs(_closest-target):
                    _closest = _sum
                if _sum < target:
                    left += 1
                else:
                    right -= 1
        return _closest