class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0 and len(nums2) != 0:
            return nums2
        if len(nums1) != 0 and len(nums2) == 0:
            return nums1
            
        m, n, k = m-1, n-1, m + n - 1

        for i in range(k, -1, -1):
            if n < 0:
                break
            if m >=0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else :
                nums1[i] = nums2[n]
                n -= 1
        
        print(nums1)