class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i, val in enumerate(nums):
            hashmap.update({val:i})
        
        result = []
        for i, val in enumerate(nums):
            _diff = target - val
            if _diff in hashmap and hashmap.get(_diff) != i:
                result.extend([i, hashmap.get(_diff)])
                break
        return result
        