from typing import List
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  
        queue = deque(nums)

        if len(nums) < 2: 
            result.append(nums)
            return result
        if len(nums) == 2:
            result.append(list(nums))
            nums[0], nums[1] = nums[1], nums[0]   
            result.append(list(nums))
            return result

        for _ in range(len(nums)):
            num = queue.popleft()
            subs = self.permute(list(queue))
            for sublist in subs:
                sublist.insert(0,num)
                result.append(sublist)
            queue.append(num)
    
        return result        