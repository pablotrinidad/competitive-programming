"""InterviewBit.

Programming > Arrays > Merge intervals.
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return '['+str(self.start)+','+str(self.end)+']'

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, n):
        r = []
        for i in range(len(intervals)):
            s = intervals[i]
            if max(s.start, n.start) > min(s.end, n.end):
                if s.start > n.start:
                    r.append(n)
                    return r + intervals[i:]
                else:
                    r.append(s)
            else:
                n.start = min(n.start, s.start)
                n.end = max(n.end, s.end)
                if n.end == s.end:
                    r.append(n)
                    return r + intervals[i+1:]
        r.append(n)
        return r

# A = [
#     Interval(6037774, 6198243),
#     Interval(6726550, 7004541),
#     Interval(8842554, 10866536),
#     Interval(11027721, 11341296),
#     Interval(11972532, 14746848),
#     Interval(16374805, 16706396),
#     Interval(17557262, 20518214),
#     Interval(22139780, 22379559),
#     Interval(27212352, 28404611),
#     Interval(28921768, 29621583),
#     Interval(29823256, 32060921),
#     Interval(33950165, 36418956),
#     Interval(37225039, 37785557),
#     Interval(40087908, 41184444),
#     Interval(41922814, 45297414),
#     Interval(48142402, 48244133),
#     Interval(48622983, 50443163),
#     Interval(50898369, 55612831),
#     Interval(57030757, 58120901),
#     Interval(59772759, 59943999),
#     Interval(61141939, 64859907),
#     Interval(65277782, 65296274),
#     Interval(67497842, 68386607),
#     Interval(70414085, 73339545),
#     Interval(73896106, 75605861),
#     Interval(79672668, 84539434),
#     Interval(84821550, 86558001),
#     Interval(91116470, 92198054),
#     Interval(96147808, 98979097),

# ]
# A = Solution().insert(A, Interval(36210193, 61984219))
A = [
    Interval(1, 2),
    Interval(8, 10),
]
A = Solution().insert(A, Interval(3, 6))
for i in A:
    print(i)
