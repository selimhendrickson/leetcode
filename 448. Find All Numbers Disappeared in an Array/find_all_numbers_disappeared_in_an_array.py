from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingNumbers = []
        i = 0

        while i < len(nums):
            num =  nums[i]
            if nums[i] != nums[num-1]: 
                nums[i], nums[num-1] = nums[num-1], nums[i] # swap numbers
            else:
                i += 1

        missingNumbers = [ind+1 for ind, val in enumerate(nums) if ind+1 != val]
    
        return missingNumbers        