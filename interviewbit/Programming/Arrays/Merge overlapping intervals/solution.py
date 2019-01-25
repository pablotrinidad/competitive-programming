"""InterviewBit.

Programming > Arrays > Merge overlapping intervals.
"""


class Interval:
    """Definition for an interval."""

    def __init__(self, s=0, e=0):
        """Constructor method."""
        self.start = s
        self.end = e


class Solution:
    """Solution."""

    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        """Merge intervals."""
        intervals = sorted(intervals, key=lambda x: x.start)
        result = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i].start <= result[-1].end:
                result[-1].end = max(intervals[i].end, result[-1].end)
            else:
                result.append(intervals[i])
        return result

