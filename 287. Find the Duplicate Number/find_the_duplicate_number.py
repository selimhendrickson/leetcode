from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            j = nums[i]
        
            if nums[i] != nums[j-1]:
                nums[i], nums[j-1] =  nums[j-1], nums[i]
            else:
                if nums[i] != i+1:
                    return nums[i]
                i += 1

        return -1