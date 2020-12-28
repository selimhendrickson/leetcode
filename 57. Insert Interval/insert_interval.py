from typing import List

#Doesn't work
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []

        if not intervals and newInterval:
            merged.append(newInterval)

        for interval in intervals:
                
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

            if newInterval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], newInterval[1])
                merged[-1][0] = min(merged[-1][0], newInterval[0])

        if merged[-1][1] < newInterval[0]:
            merged.append(newInterval)

        return merged