from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # the intuition is that one side of the array should be sorted. By looking for that, we'll "squeeze" target in mid.
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # we found the target
                return mid
            if nums[left] <= nums[mid]:
                # left side of array is sorted
                if nums[left] <= target <= nums[mid]:
                    # target is in left side so move the right
                    right = mid - 1
                else:
                    # target is in right side
                    left = mid + 1
            else:
                # right side of the array should be sorted
                if nums[mid] <= target <= nums[right]:
                    # target is in right side so move
                    left = mid + 1
                else:
                    # target is in right side
                    right = mid - 1

        # we are not able to find the element in the given array
        return -1 