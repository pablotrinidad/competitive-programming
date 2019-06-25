// InterviewBit.
// Programming > Arrays > K-th row of Pascal's Triangle.

package main

import "fmt"

func main() {
	for n := 0; n < 10; n++ {
		fmt.Println("N:", n)
		R := solve(n)
		for _, e := range R {
			fmt.Printf("\t%v\n", e)
		}
	}
}

/**
 * @input A : Integer
 *
 * @Output 2D int array.
 */
func solve(A int) [][]int {
	R := make([][]int, A)
	for rowSize, row := range R {
		if rowSize+1 > 1 {
			row = append(row, 1)
		}
		for i := 1; i < rowSize; i++ {
			row = append(row, R[rowSize-1][i]+R[rowSize-1][i-1])
		}
		row = append(row, 1)
		R[rowSize] = row

	}
	return R
}
