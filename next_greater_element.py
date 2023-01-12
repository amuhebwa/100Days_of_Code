class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        results = []
        for  _, val1 in enumerate(nums1):
            if val1 in nums2:
                index_of_v1 = nums2.index(val1)
                next_index = index_of_v1 + 1 
                if next_index < len(nums2) and nums2[next_index] > val1:
                    results.append(nums2[next_index])
                else:
                    results.append(-1)
        return results
        '''
        results = []
        for _, val1 in enumerate(nums1):
            index_of_v1 = nums2.index(val1)
            sub_arr = nums2[index_of_v1:]
            max_val = -1
            if index_of_v1 == len(nums2)-1 or len(sub_arr) == 0:
                max_val = -1
            else:
                while len(sub_arr):
                    current_val = sub_arr.pop()
                    if  current_val > val1:
                        max_val = current_val
            results.append(max_val)
        
        return results


               
