// InterviewBit
// Programming > Arrays > Add one to number

package main

import "fmt"

func main() {
	// A := []int{1, 2, 3}
	// A := []int{}
	A := []int{0, 0, 9, 7}
	fmt.Println(plusOne(A))
}

/**
 * @input A : Integer array
 *
 * @Output Integer array.
 */
func plusOne(A []int) []int {
	// Add zero in case sum overflows
	A = append([]int{0}, A...)

	// Keep adding one until addition stops carrying
	for i := len(A) - 1; i >= 0; i-- {
		A[i] = (A[i] + 1) % 10
		if A[i] != 0 {
			break
		}

	}

	// Remove leading zeros
	startingIndex := 0
	for i, e := range A {
		if e != 0 {
			break
		}
		startingIndex = i + 1
	}
	return A[startingIndex:]
}
