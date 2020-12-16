from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        for num in nums:
            if num == 1:                
                count += 1
            else:
                # Find the maximum till now.
                if count > max_count:
                    max_count = count                                
                count = 0
        if count > max_count:
                    max_count = count                                
        return max_count