from typing import List

class Solution:    
    def removeElement(self, nums: List[int], val: int) -> int:
        right_index = len(nums)-1        
        result = 0
        
        for index in range(len(nums)):
            if nums[index] == val:
                while nums[right_index] == val and right_index > index:
                    right_index -= 1
                if index == right_index:
                    result = index
                    break
                else:
                    nums[index] = nums[right_index]         
                    right_index -= 1
            else:
                result += 1
            
        return result