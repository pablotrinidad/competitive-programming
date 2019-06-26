// InterviewBit
// Programming > Arrays > Repeat and Missing Number Array

package main

import "fmt"

func main() {
	A := []int{3, 1, 2, 5, 3}
	fmt.Println(repeatedNumber(A))
}

/**
 * @input A : Integer array
 *
 * @Output Integer array.
 */
func repeatedNumber(L []int) []int {
	R := make([]int, len(L))
	a, b := 0, 0
	for _, e := range L {
		R[e-1]++
	}
	for i, e := range R {
		if e == 2 {
			a = i + 1
		}
		if e == 0 {
			b = i + 1
		}
	}
	return []int{a, b}
}
