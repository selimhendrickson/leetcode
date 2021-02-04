from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for i in nums[1:]:
            num ^= i
        return num