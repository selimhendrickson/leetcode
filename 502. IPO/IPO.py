from heapq import *
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        minCapitalHeap = [(Capital[i],i) for i in range(len(Capital))]
        heapify(minCapitalHeap)
        maxProfitHeap = []
        totalCapital = W

        for _ in range(k):
            while minCapitalHeap and minCapitalHeap[0][0] <= totalCapital:
                capital, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-Profits[i], i))

            if not maxProfitHeap: break

            totalCapital += -heappop(maxProfitHeap)[0]
        
        return totalCapital