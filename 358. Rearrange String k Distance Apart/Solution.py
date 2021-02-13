from collections import Counter, deque
from heapq import *

class Solution:
    def rearrangeString(self, S: str, d: int) -> str:
        counter = Counter(S)

        maxheap = []
        minheap = []
        result = []  
        index = 0 

        for k, v in  counter.items():    
            heappush(maxheap, [-v, k])

        while maxheap:
            item = heappop(maxheap)
            v, k = -item[0], item[1]
            result += k
            v -= 1
            if v > 0:
                heappush(minheap, [index+d, [-v, k]])
            index += 1

            if minheap and minheap[0][0] <= index:
                item = heappop(minheap)[1]
                heappush(maxheap, item)
    
        return ''.join(result) if len(result) == len(S) else ""        

    def rearrangeString2(self, S: str, k: int) -> str:
        if k <= 1: 
            return S

        charFrequencyMap = {}
        for char in S:
            charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

        maxHeap = []
        # add all characters to the max heap
        for char, frequency in charFrequencyMap.items():
            heappush(maxHeap, (-frequency, char))

        queue = deque()
        resultString = []
        while maxHeap:
            frequency, char = heappop(maxHeap)
            # append the current character to the result string and decrement its count
            resultString.append(char)
            # decrement the frequency and append to the queue
            queue.append((char, frequency+1))
            if len(queue) == k:
                char, frequency = queue.popleft()
                if -frequency > 0:
                    heappush(maxHeap, (frequency, char))

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(resultString) if len(resultString) == len(S) else ""    

    def rearrangeString3(self, S: str, d: int) -> str:
        if d <= 1: return S
        
        counter = Counter(S)

        maxheap = []
        queue = deque()
        result = []          

        for k, v in  counter.items():    
            heappush(maxheap, (-v, k))

        while maxheap:            
            v, k = heappop(maxheap)
            result += k            
            queue.append((k, v+1))

            if len(queue) == d:
                k, v = queue.popleft()
                if -v > 0:
                    heappush(maxheap, (v, k))
    
        return ''.join(result) if len(result) == len(S) else ""         