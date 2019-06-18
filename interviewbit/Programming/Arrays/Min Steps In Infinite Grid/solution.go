// Problem statement: https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
package main

import (
	"fmt"
	"math"
)

func main() {
	// A := []int{0, 1, 1}
	// B := []int{0, 1, 2}

	// A := []int{-2}
	// B := []int{7}

	A := []int{4, 8, -7, -5, -13, 9, -7, 8}
	B := []int{4, -15, -10, -3, -13, 12, 8, -8}
	fmt.Println(coverPoints(A, B))
}

func coverPoints(A []int, B []int) int {
	x, y := A[0], B[0]
	d := 0.0
	for i := range A {
		dx := math.Abs(float64(x) - float64(A[i]))
		dy := math.Abs(float64(y) - float64(B[i]))
		d += math.Max(dx, dy)
		x, y = A[i], B[i]
	}
	return int(d)
}
