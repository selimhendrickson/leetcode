from typing import List
from heapq import * 

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
             
        if len(sticks) == 1 : return 0 
        
        result = 0   
        heapify(sticks)
        
        while len(sticks) > 1:
            num1 = heappop(sticks)
            num2 = heappop(sticks)
            result += num1 + num2
            heappush(sticks, num1 + num2)

        return result        