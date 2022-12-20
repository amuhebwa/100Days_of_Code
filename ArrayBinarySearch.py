import numpy as np

def binsearch(A, key, low, high):
    if high >= low:
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        elif A[mid] > key: # search left
            binsearch(A, key, low, mid-1)
        else: # search right
            binsearch(A, key, mid+1, high)
    return -1

if __name__=="__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 9
    low = 0
    high = len(A)-1
    print(binsearch(A, key, low, high))
