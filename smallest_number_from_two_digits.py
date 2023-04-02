class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        res = [45, 51, 57]
        '''
        nums1.sort()
        nums2.sort()
        
        sub = list(set(nums1).intersection(nums2))
        if len(sub) != 0:
            return min(sub)
        else:
            result =set()
            for i in nums1:
                for j in nums2:
                    result.add(int(str(i)+str(j)))
            #for i in nums2:
            #    for j in nums1:
                    result.add(int(str(j)+str(i)))
            return min(result)