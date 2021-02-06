from heapq import *
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxheap = []        
        
        for point in points:
            if K > 0: 
                distance = point[0] ** 2 + point[1] ** 2
                heappush(maxheap, [-distance, point])   
            else: 
                distance = point[0] ** 2 + point[1] ** 2
                heappushpop(maxheap, [-distance, point])                   
            K -= 1
        
        return [maxheap[0][1]]