class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        l, r, n = 0, len(citations)-1, len(citations)
        while l < r:
            mid = l + (r-l)//2
            if citations[mid] >= n-mid:
                r = mid
            else:
                l = mid + 1
        
        return 0 if citations[l] == 0 else n-l