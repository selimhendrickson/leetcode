from typing import List
from heapq import *

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        minheap = [[abs(x-num), num] for num in arr]
        heapify(minheap)

        for _ in range(k):
            result.append(heappop(minheap)[1])
  
        result.sort()

        return result