class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        # This solution works, but fails the time limit on a large array
        results = []
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = 1
            p = prod(nums)
            results.append(p)
            nums[i] = temp
        return results
        '''
        left_arr, right_arr = [1]*len(nums), [1]*len(nums)
        left_arr[0], right_arr[len(nums)-1] = nums[0], nums[len(nums)-1]
        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i-1]*nums[i]
        
        for j in range(len(nums)-2, -1, -1):
            right_arr[j] = nums[j]* right_arr[j+1]

        # print(left_arr)
        # print('-'*10)
        # print(right_arr)
        pre_fix, post_fix, results = 1, 1, []
        for i in range(len(nums)):
            prefix = left_arr[i-1] if (i-1) >= 0 else 1
            postfix = right_arr[i+1] if (i+1) < len(nums) else 1
            results.append(prefix * postfix)
        return results
        