from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)        

        while start < end:
            middle = start + (end - start) // 2
            num = nums[middle]
            if num == target: return middle
            if num < target:
                start = middle + 1
            if num > target:
                end = middle

        return -1
        

