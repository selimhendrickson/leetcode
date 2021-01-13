from heapq import *
class Solution:
    def __init__(self):
        self.minheap, self.maxheap = [], []    
        
    def medianSlidingWindow(self, nums, k):
        result = []
        left, right = 0, 0

        while right < k:      
            self.insert_num(nums[right])
            right += 1
    
        result.append(self.find_median())

        while right < len(nums):
            self.remove_num(nums[left])
            self.insert_num(nums[right])
            result.append(self.find_median())
            left, right = left+1, right+1

        return result
  
    def insert_num(self, num):
        if not self.maxheap or num <= -self.maxheap[0]:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        self.balance_heaps()

    def remove_num(self, num):        
        if num <= -self.maxheap[0]:
            heap = self.maxheap
            i = self.maxheap.index(-num)
        else:
            heap = self.minheap
            i = self.minheap.index(num)
        heap[i] = heap[-1]
        heap.pop()
        heapify(heap)
            
        self.balance_heaps()

    # Checked
    def balance_heaps(self):
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))            

    def find_median(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]      