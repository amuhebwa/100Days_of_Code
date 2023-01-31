def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)
if __name__ == "__main__":
    data = [8, 7, 2, 1, 0, 9, 6]
    print("Unsorted Array")
    print(data)
    n = len(data) - 1
    quickSort(data, 0, n)
    print("sorted")
    print(data)
