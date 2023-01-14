class Solution:
    def swap_elements(self, arr, p1, p2):
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
    def sortColors(self, nums: List[int]) -> None:
        '''
        Note: This is a brute solution. works inplace but has a quadratic running time complexity
        Note: I could also run a quick sort with o(nlog n) time complexity
        n = len(nums)
        for i in range(0, n):
            min_index = i 
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            temp = nums[i]
            nums[i]=nums[min_index]
            nums[min_index] = temp
        
        print(nums)
        '''
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                pass