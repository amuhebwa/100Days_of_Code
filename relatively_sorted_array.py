class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # arr1 = [2,3,1,3,2,4,6,7,9,2,19]
        # arr2 = [2,1,4,3,9,6]
        # 2, 2,2, 1, 4, 3,3, 9, 6, 7, 19
        results = []
        for val in arr2:
            for current_val in arr1:
                if val == current_val:
                    results.append(current_val)
        
        for val in results:
            if val in arr1:
                arr1.remove(val)
        
        arr1.sort()
        results = results + arr1
        return results