#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def calculate_medium(arr):
    if arr == []:
        return 0
    if len(arr) == 1:
        return arr[0]
    l = len(arr)
    if l%2 ==0:
        return (arr[l//2] + arr[(l//2 - 1)])/2
    else:
        return arr[l//2]
def activityNotifications(expenditure, d):
    # Write your code here
    if len(expenditure) <= d:
        return 0
    if len(expenditure) <= 1:
         return 0
    
    n = len(expenditure)
    count = 0
    for i in range(d, n):
        start = i-d if i < n-1 else i-d+1
        end = i if i < n-1 else n
        curr_arr = expenditure[start:end]
        curr_arr.sort()
        print('x ->', curr_arr, ' | ', expenditure[i])
        med = calculate_medium(curr_arr)
        if expenditure[i] >= med*2:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
