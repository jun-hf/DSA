package main

import "fmt"

var primes = []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

func binarySearch(arr []int, target int) (int, error) {
	min := 0 
	max := len(arr) - 1

	for ;min <= max; {
		mid := min + (max - min) / 2

		if arr[mid] > target {
			max = mid -1
			continue
		}

		if arr[mid] < target {
			min = min + 1
			continue
		}

		if arr[mid] == target {
			return mid, nil
		}
	}

	return -1, fmt.Errorf("target (%v) is not in arr", target)
}

func main() {
	if n, err := binarySearch(primes, 67); n != 18 || err != nil {
		panic("target 67 should be 18")
	}

	if n, err := binarySearch(primes, 3); n != 1 || err != nil {
		panic("target 3 should be 1")
	}

	if n, err := binarySearch(primes, 89); n != 23 || err != nil {
		panic("target 89 should be 23")
	}

	if n, err := binarySearch(primes, 24); n != -1 || err == nil {
		panic("target 24 should be -1")
	}

	if n, err := binarySearch(primes, 99); n != -1 || err == nil {
		panic("target 99 should be -1")
	}
}