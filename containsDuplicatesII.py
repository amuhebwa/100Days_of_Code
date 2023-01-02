class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Brute Force
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j] and abs(i-j) <= k:
                    return True
    
        return False
        """
        lookup = {}
        for i, val in enumerate(nums):
            if val in lookup and lookup.get(val) != i and abs(lookup.get(val) - i) <= k:
                return True
            else:
                lookup.update({val:i})
        
        return False