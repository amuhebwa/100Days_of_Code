def merge_sort(nums):
   if len(nums) > 1:
       mid = len(nums)//2
       left_arr = nums[:mid]
       right_arr = nums[mid:]
       merge_sort(left_arr)
       merge_sort(right_arr)
       i, j, k = 0, 0, 0
       while i < len(left_arr) and j < len(right_arr):
           if left_arr[i] < right_arr[j]:
               nums[k] = left_arr[i]
               i += 1
           else:
               nums[k] = right_arr[j]
               j += 1
           k += 1
       # copy the remaining elements in the left/right array
       while i < len(left_arr):
           nums[k] = left_arr[i]
           k += 1
           i += 1
       while j < len(right_arr):
           nums[k] = right_arr[j]
           k += 1
           j += 1
   return nums



if __name__== "__main__":
    arr = [1,6,7,8,5,3,4,0,9]
    print(arr)
    print('-'*10)
    print(merge_sort(arr))
