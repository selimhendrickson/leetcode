from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """        
        index = 0
        while index < len(arr):            
            if arr[index] == 0:
                index2 = len(arr)-1
                while index2 > index:
                    arr[index2] = arr[index2-1]
                    index2 -= 1
                index += 1
            index += 1
                
                    
                    
                    
                
                
                
        