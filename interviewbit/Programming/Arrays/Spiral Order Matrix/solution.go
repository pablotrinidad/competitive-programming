// InterviewBit
// Programming > Arrays > Spiral Order Matrix

package main

import "fmt"

func main() {
	A := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Println(spiralOrder(A))
}

func spiralOrder(A [][]int) []int {
	dir := 1 // 1:l->r, 2: t->b, 3: r->l, 4: b->t
	m, n := len(A), len(A[0])
	top, left, bottom, right := 0, 0, m-1, n-1
	B := make([]int, m*n)
	k := 0
	for top <= bottom && left <= right {
		switch dir {
		case 1:
			{
				for i := left; i <= right; i++ {
					B[k] = A[top][i]
					k++
				}
				top++
				dir = 2
			}
		case 2:
			{
				for i := top; i <= bottom; i++ {
					B[k] = A[i][right]
					k++
				}
				right--
				dir = 3
			}
		case 3:
			{
				for i := right; i >= left; i-- {
					B[k] = A[bottom][i]
					k++
				}
				bottom--
				dir = 4
			}
		case 4:
			{
				for i := bottom; i >= top; i-- {
					B[k] = A[i][left]
					k++
				}
				left++
				dir = 1
			}

		}
	}
	return B
}
