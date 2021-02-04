from typing import List

class Solution:
    def findComplement(self, num: int) -> int:
        bit = 1       
        num ^= bit
        while bit < num:            
            bit = bit << 1
            num ^= bit
      
        return num