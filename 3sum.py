class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    curr_sum = nums[i] + nums[j] + nums[k]
                    if i !=j and i !=k and j != k and curr_sum == 0:
                        curr_res =[nums[i], nums[j], nums[k]]
                        curr_res.sort()
                        if curr_res not in result:
                            result.append(curr_res)
        return result
        '''
        '''
        credit: Neetcode helped me figure out the final solution. 
        '''
        nums.sort()
        n = len(nums) - 1
        result = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            left, right = i+1, n
            while left < right:
                _sum = val + nums[left] + nums[right]
                if  _sum == 0:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        #right -= 1
                elif _sum < 0:
                    left += 1
                else:
                    right -= 1
        return result
        