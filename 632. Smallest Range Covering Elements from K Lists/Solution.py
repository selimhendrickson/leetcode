from heapq import heappush, heappop, heapify
from typing import List
import math

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lower = 0
        upper = math.inf
        minheap = []
        currentMax = -math.inf

        for arr in nums:
            heappush(minheap, (arr[0], 0, arr))
            currentMax = max(currentMax, arr[0])

        while len(minheap) == len(nums):
            val, index, arr = heappop(minheap)

            if upper - lower > currentMax - val:
                lower = val
                upper = currentMax
            
            if len(arr) > index + 1:
                heappush(minheap, (arr[index+1], index+1, arr))
                currentMax = max(currentMax, arr[index+1])


        return [lower, upper]        