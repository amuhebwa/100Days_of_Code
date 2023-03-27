# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        I was stuck along the way and the solution by 
        Aleksei Mamaev helped me figure out the last part
        '''
        l, r = 0, n
        first_ind = 1
        while l <= r:
            mid = int((l+r)//2)
            if isBadVersion(mid):
                r = mid-1
                first_ind = mid
            else:
                l = mid + 1
        return first_ind