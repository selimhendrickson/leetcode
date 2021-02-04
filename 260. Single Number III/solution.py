from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num
        
        rightmost = 1
        while(n1xn2 & rightmost) == 0:
            rightmost = rightmost << 1
            
        n1, n2 = 0, 0
        
        for num in nums:
            if (num & rightmost) != 0:
                n1 ^= num
            else:
                n2 ^= num
                
        return [n1, n2]