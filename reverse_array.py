def reverse_array(arr):
    start=0
    end = len(arr) - 1
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

if __name__=="__main__":
    arr = [10, 20, 30, 40, 50]
    print(arr)
    print('-'*30)
    print(reverse_array(arr))
