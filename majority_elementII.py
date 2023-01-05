class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        T = len(nums)//3
        table = Counter(nums)
        vals = [*table.keys()]
        results = []
        for val in vals:
            if table.get(val) > T:
                results.append(val)
        
        return results