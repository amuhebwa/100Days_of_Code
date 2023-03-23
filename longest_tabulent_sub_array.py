class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        There is an optimized solution that uses Dynamic programming. 
        Since we have not covered it, i am leaving it here for future reference 
        https://youtu.be/wfbVp8hTVX8
        '''
        i, j, max_len = 0, 0, 0
        n = len(arr)
        if n == 1:
            return 1
        
        while j < n:
            while (j < n-1) and (arr[j-1] > arr[j] < arr[j + 1] or arr[j-1] < arr[j] > arr[j+1]):
                j += 1
            while (i < j) and (arr[i] == arr[i+1]):
                i += 1
            max_len = max(max_len, j-i+1)
            i = j
            j += 1
        return max_len