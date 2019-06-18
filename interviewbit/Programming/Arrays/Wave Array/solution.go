package main

import (
	"fmt"
	"sort"
)

func main() {
	A := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
	fmt.Println(wave(A))
}

/**
 * @input A : Integer array
 *
 * @Output Integer array.
 */
func wave(A []int) []int {
	sort.Ints(A)
	R := make([]int, len(A))
	for i := range R[:len(A)-(len(A)%2)] {
		R[i] = A[i^1]
	}
	if len(A)%2 == 1 {
		R[len(A)-1] = A[len(A)-1]
	}
	return R
}
