from collections import Counter
from heapq import *

class Solution:
    def reorganizeString(self, S: str) -> str:
        # Use counter to count the frequencies. 
        counter = Counter(S)
    
        maxheap = []
        result = []
        last = None

        # Push counted chars into maxheap. Use negative values to use the heapq as a maxheap. 
        for k, v in  counter.items():    
            heappush(maxheap, [-v, k])

        while maxheap:
            # Pop the most frequent letter.
            item = heappop(maxheap)
            v, k = -item[0], item[1]
            result += k
            # Decrease frequency now that we used it 
            v -= 1
            
            # This line is the key. If we push it back right after using, it's going to be popped again 
            # in the next iteration resulting in the same letter being adjacent.            
            if last: heappush(maxheap, last)
                
            # If the count is more than 0, we can pop it back into the heap - in the next iteration
            if v > 0: last = [-v, k] 
            else: last = None

        # If the final string is the same length as input, return it. If now, then we failed.        
        return ''.join(result) if len(result) == len(S) else ""