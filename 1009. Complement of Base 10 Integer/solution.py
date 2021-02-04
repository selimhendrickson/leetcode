class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bit = 1       
        N ^= bit
        while bit < N:            
            bit = bit << 1
            N ^= bit
      
        return N        