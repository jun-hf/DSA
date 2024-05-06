import math 
from typing import List 
import binaryTest

def bs(arr: List[int], target: int):
    min = 0
    max = len(arr)

    return recur_binary_search(min, max, arr, target)

def recur_binary_search(min: int, max: int, arr: List[int], target: int):
    if max < min:
        return -1
    mid = int(min + math.floor((max-min)/2))
    mid_val = arr[mid]

    if mid_val == target: 
        return mid
    
    if mid_val < target:
        return recur_binary_search(mid+1, max, arr, target)
    if mid_val > target:
        return recur_binary_search(min, mid-1, arr, target)
    
binaryTest.test(bs)