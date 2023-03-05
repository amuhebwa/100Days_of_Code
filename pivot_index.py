class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)-1
        pivot = -1
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            #print(nums[:i], nums[i+1:])
            if left == right:
                pivot = i
                break

        return pivot