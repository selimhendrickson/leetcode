# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []
        merged_intervals = []

        #flatten intervals
        merged_intervals = [val for sublist in schedule for val in sublist]
    
        merged_intervals.sort(key=lambda x: x.start)

        end = merged_intervals[0].end
        for interval in merged_intervals[1:]:
            if interval.start > end: 
                result.append(Interval(end, interval.start))
            end = max(end, interval.end)

        return result        
        