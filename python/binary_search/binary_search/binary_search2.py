import math
import binaryTest

# we got an arr = [3, 4, 9, 19] sorted and given target
#  I need to find the index of target in arr

# since we know that arr is sorted, take the mid point compute from the start and end
# and compare the mid point to target.

# if the mid point value is bigger than target, we know that anything larger than mid point is invalid so we make max to mid - 1
# if the mid point value is smaller than target, we know that any guess smaller than mid value will be wrong so we can set min = mid + 1
# if mid point == target, we have found the index

# we just need to repeat the process until we find target's index, until max < min
# in that case target is not in the arr
def binary_search(arr, target):
    min = 0 
    max = len(arr) -1 

    while not (max < min):
        mid = int(min + math.floor((max - min)/2))
        mid_value = arr[mid]

        if mid_value > target:
            max = mid - 1
            continue
        if mid_value < target:
            min = mid + 1
            continue
        if mid_value == target:
            return mid
    return -1

binaryTest.test(binary_search)