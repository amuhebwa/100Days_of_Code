class Solution:
    def flip(self, arr, j):
        i = 0
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i+= 1
            j-=1
    
    def find_index(self, arr, val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i
        return -1
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        Struggled to solve this on my own. 
        credit: https://youtu.be/4WQouWU9XXE for good explanation and walk through
        '''
        if not arr or len(arr) == 0:
            return arr
        
        result, n = [], len(arr)
        
        for indx in range(n):
            max_ = max(arr[:n - indx])
            max_indx = arr.index(max_) + 1
            arr[:max_indx] = reversed(arr[:max_indx])
            result.append(max_indx)
            
            arr[:n - indx] = reversed(arr[:n - indx])
            result.append(n - indx)
        return result