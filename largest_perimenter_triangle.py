class Solution:
    def check_condition(self, side1, side2, side3):
        return side1 + side2 > side3
    def largestPerimeter(self, nums: List[int]) -> int:
        # condition of the triangle: the sum of two smaller sides > big side
        nums.sort()
        total_area = 0
        for i in range(0, len(nums)-2):
            if self.check_condition(nums[i], nums[i+1], nums[i+2]):
                total_area = nums[i] + nums[i+1] + nums[i+2]
        return total_area