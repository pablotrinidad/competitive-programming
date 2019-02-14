"""InterviewBit.

Programming > Strings > Palindrome String.
"""


class Solution:
    """Solution."""

    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        """Solution."""
        A = A.lower()
        start, end = 0, len(A) - 1
        while start <= end:
            s, e = A[start], A[end]
            if not s.isalnum():
                start += 1
            elif not e.isalnum():
                end -= 1
            else:
                if s != e:
                    return 0
                start += 1
                end -= 1
        return 1


print('solution', Solution().isPalindrome("A man, a plan, a canal: Panama"))
