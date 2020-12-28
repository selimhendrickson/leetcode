from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_rooms = 1
        rooms = []
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            for room in rooms:
                if room <= intervals[i][0]: 
                    rooms.remove(room)
            
            rooms.append(intervals[i][1])                 

            max_rooms = max(len(rooms),max_rooms)

        return max_rooms

