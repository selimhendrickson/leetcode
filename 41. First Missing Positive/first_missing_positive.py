from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        
        i = 0

        while i < len(nums):
            j = nums[i]
            if j > 0 and j <= len(nums) and nums[i] != nums[j-1]:
                nums[i], nums[j-1] = nums[j-1], nums[i]
            else:
                i += 1

        for i in range(1, len(nums)+1):
            if i != nums[i-1]: return i
  
        return i + 1       