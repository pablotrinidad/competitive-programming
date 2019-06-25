// InterviewBit
// Programming > Arrays > MAXSPROD

package main

import "fmt"

func main() {
	// A := []int{15, 44, 0, 23, 26, 46, 16, 28, 34, 4}
	A := []int{6, 7, 9, 5, 5, 8}
	fmt.Println(maxSpecialProduct(A))
}

func cleanStack(A []int, stack []int, ref int) []int {
	n := len(stack)
	for n-1 >= 0 {
		if A[stack[n-1]] <= ref {
			stack = stack[:n-1]
			n--
		} else {
			break
		}
	}
	return stack
}

func getSpecial(stack []int) int {
	n := len(stack)
	if n == 0 {
		return 0
	}
	return stack[n-1]
}

/**
 * @input A : Integer array
 *
 * @Output Integer
 */
func maxSpecialProduct(A []int) int {
	msp := 0
	n := len(A)
	lsv, rsv := make([]int, n), make([]int, n) // Left/Right Special Values
	lStack, rStack := []int{}, []int{}
	for i := 0; i < n; i++ {
		// Right index
		rI := n - 1 - i

		// Clean stacks
		lStack = cleanStack(A, lStack, A[i])
		rStack = cleanStack(A, rStack, A[rI])

		// Update special values
		lsv[i] = getSpecial(lStack)
		rsv[rI] = getSpecial(rStack)

		// Append current element to stack
		lStack = append(lStack, i)
		rStack = append(rStack, rI)
	}

	// Find max special value
	for i := 0; i < n; i++ {
		if (lsv[i] * rsv[i]) > msp {
			msp = lsv[i] * rsv[i]
		}
	}
	return msp % 1000000007
}
