from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for value in A:
            B.append(value**2)
        return sorted(B)