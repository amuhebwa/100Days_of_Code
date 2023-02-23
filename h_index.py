class Solution:
    def reverse(self, arr):
        i, j = 0, len(arr)-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
    def hIndex(self, citations: List[int]) -> int:
        """
        The optimal solution is using heaps, but i couldn't solve it that way
        Followed one of the solutions (easiest to understand)
        """
        n = len(citations)
        citations.sort()
        citations = self.reverse(citations)
        for i in range(n):
            if citations[i] <= i:
                return i
        return n