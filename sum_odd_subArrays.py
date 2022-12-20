class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        results = []
        odd_index, n = 1, len(arr)

        while odd_index <= n:
            # do some stuff
            for i in range (0, len(arr)):
                window_size = i+odd_index
                if window_size <= n:
                    results.extend(arr[i:window_size])
            odd_index += 2
        
        _sum = sum(results)
        return _sum