def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
        #nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


if __name__=="__main__":

    nums = [2,4,5,1,3,9,7,8,6]
    print(nums)
    result = selection_sort(nums)

    print("-"*20)
    print(result)
