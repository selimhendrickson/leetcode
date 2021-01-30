from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [- 1, -1]
        if not nums: return result
        result[0] = self.binarySearch(nums, target, False)
        if result[0] != -1: 
            result[1] = self.binarySearch(nums, target, True)
        return result
  

    def binarySearch(self, arr, key, findMaxIndex):
        start, end = 0, len(arr) - 1
        index = -1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] > key:
                end = mid - 1
            elif arr[mid] < key:
                start = mid + 1
            else:
                index = mid
                if findMaxIndex:
                    start = mid + 1
                else:
                    end = mid - 1

        return index 