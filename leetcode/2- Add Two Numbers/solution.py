class Solution:
    def addTwoNumbers(self, A: ListNode, B: ListNode) -> ListNode: 
        carry = 0
        r = ListNode(0)
        L = r
        while A or B or carry:
            a = A.val if A else 0
            b = B.val if B else 0
            carry, s = divmod(a + b + carry, 10)
            
            L.next = ListNode(s)
            L = L.next
            

            A = None if not A else A.next
            B = None if not B else B.next

        return r.next