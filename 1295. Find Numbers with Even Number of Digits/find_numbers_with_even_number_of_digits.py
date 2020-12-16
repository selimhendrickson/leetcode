from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        string = ""
        result = 0
        for value in nums:
            string = str(value)
            if len(string) % 2 == 0:
                result += 1
        return result