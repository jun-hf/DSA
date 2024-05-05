from typing import List
import binaryTest
import math

def ds(arr: List[int], target: int):
    min = 0
    max = len(arr)

    while not (max < min):
        mid = int(min + math.floor((max - min)/2))
        mid_value = arr[mid]

        if mid_value > target:
            max = mid -1
            continue
        if mid_value < target:
            min = mid + 1
            continue
        if mid_value == target:
            return mid
        
    return -1

binaryTest.test(ds)