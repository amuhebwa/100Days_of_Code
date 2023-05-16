class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        if not nums:
            return 0
        counter, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                curr_sum = sum(nums[i:j+1])
                if curr_sum == k:
                    counter += 1
        return counter
        '''
        '''
        I kept getting timeout. 
        Credit to one code man: https://www.youtube.com/watch?v=EFzYA9H0MfQ&ab_channel=OneCodeMan 
        for a good solution which guided me into getting a correct submission. 
        '''
        counter ,curr_sum, n = 0, 0, len(nums)
        lookup = dict()
        lookup[0] = 1
        for i in range(n):
            curr_sum += nums[i]
            _diff = curr_sum - k
            if _diff in lookup:
                counter += lookup[_diff]
            lookup[curr_sum] = lookup.get(curr_sum, 0) + 1
        return counter