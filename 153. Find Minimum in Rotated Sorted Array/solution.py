from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The smallest number is the rotation pivot
        left, right = 0 , len(nums) - 1
  
        if nums[left] <= nums[right]: 
            # Array hasn't been rotated
            return nums[left]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                # we found it
                return nums[mid + 1]
            else: 
                # find which side the pivot is
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid        

    def findMin2(self, nums: List[int]) -> int:
        # The smallest number is the rotation pivot
        left, right = 0 , len(nums) - 1
  
        if nums[left] <= nums[right]: 
            # Array hasn't been rotated
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]: return nums[mid + 1]
            if nums[mid - 1] > nums[mid]: return nums[mid]
            if nums[mid] > nums[left]:
                left = mid + 1
            else: 
                right = mid -1                 