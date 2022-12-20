class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None:
            return
        if len(nums) == 1:
            return nums[0]
        _sum = 0
        for i, num in enumerate(nums):
            _sum += num
            nums[i] = _sum
        return nums

if __name__=="__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6,7]
    print(sol.runningSum(arr))
    """
    Time complexity: 0(n)
    Space complexity: 0(1)
    """
