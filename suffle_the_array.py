from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if nums is None:
            return
        if n < 2:
            return nums
        if nums == 2:
            return [nums[1], nums[0]]
        mid = int(len(nums)//2)
        results = []
        for i in range(mid):
            results.extend([nums[i], nums[mid+i]])
        return results

if __name__=="__main__":
    sol = Solution()
    arr = [2,5,1,3,4,7]
    expected = [2,3,5,4,1,7]
    n = 3
    res = sol.shuffle(arr, n)
    """
    time complexity: O(n/2) => O(n). because we have one for loop
    space complexity = O(n). because we create an additional array to append the results
    """
