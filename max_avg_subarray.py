class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n =len(nums)
        '''
        if k >= n:
            return 0
        max_val = float('-inf')
        for i in range(n):
            if (i + k) < n:
                window_sum =  mean(nums[i:i+k])
                max_val = max(max_val, window_sum)
            else:
                break
        
        '''
        max_sum, curr_sum = sum(nums[:k]), sum(nums[:k])
        for i in range(k, n):
            curr_sum += (nums[i] - nums[i-k])
            max_sum = max(curr_sum, max_sum)
        return (max_sum/k)