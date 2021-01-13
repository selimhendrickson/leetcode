from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)
        
        # balance heaps
        if len(self.maxheap) > len(self.minheap)+1:
            heappush(self.minheap, -heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))
            
            
            
            

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()