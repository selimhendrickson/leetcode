from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        missingNumbers = []
        i = 0

        while i < len(nums):
            num =  nums[i]
            if nums[i] != nums[num-1]: 
                nums[i], nums[num-1] = nums[num-1], nums[i] # swap numbers
            else:
                i += 1

        missingNumbers = [val for ind, val in enumerate(nums) if ind+1 != val]
        missingNumbers.sort()

        return missingNumbers