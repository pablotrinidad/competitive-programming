/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(A *ListNode, B *ListNode) *ListNode {
	R := &ListNode{}
	L := R
	carry := 0
	for A != nil || B != nil || carry > 0 {
		var a, b int = 0, 0
		if A != nil {
			a = A.Val
		}
		if B != nil {
			b = B.Val
		}

		s := a + b + carry
		carry = s / 10

		L.Next = &ListNode{Val: s % 10, Next: nil}
		L = L.Next

		if A != nil {
			A = A.Next
		}
		if B != nil {
			B = B.Next
		}
	}
	return R.Next
}