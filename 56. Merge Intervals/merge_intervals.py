from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0]  <= end:
                end = max(interval[1], end)
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]

        merged.append([start,end])
        return merged