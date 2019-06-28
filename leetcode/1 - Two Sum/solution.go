// LeetCode: Two sum

package main

import "fmt"

func main() {
	// A := []int{2, 7, 11, 15}
	// target := 9

	// A := []int{0, 4, 3, 0}
	// target := 0

	A := []int{-3, 4, 3, 90}
	target := 0

	fmt.Println(twoSum(A, target))
}

func twoSum(nums []int, target int) []int {
	results := make(map[int]int)
	for i, e := range nums {
		j, ok := results[e]
		if ok {
			return []int{j, i}
		}
		results[target-e] = i
	}
	return []int{0, 0}
}
