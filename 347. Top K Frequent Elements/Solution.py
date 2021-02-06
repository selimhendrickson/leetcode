from heapq import *
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topNumbers = []  
        hashmap = {}

        for num in nums:
            if num in hashmap: hashmap[num] += 1
            else: hashmap[num] = 1

        maxheap = [[-count, num] for num, count in hashmap.items()]
        heapify(maxheap)
    
        for _ in range(k):
            topNumbers.append(heappop(maxheap)[1])

        return topNumbers        