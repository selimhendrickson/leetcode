from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        
        while i < len(nums):
            num = nums[i]
            if num < n and i != num:
                nums[i], nums[num] = nums[num], num
            else:
                i += 1

        for i in range(n):
            if nums[i] == n: return i
            
        return n
