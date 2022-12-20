class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = int)

        largest = nums[-1]
        for i in range(len(nums), len(nums)-k, -1):
            largest = nums.pop()
        return largest

if __name__=="__main__":
    """
    Time complexity = O(nlogn) + O(n)
    Space complexity = 0(1)
    """