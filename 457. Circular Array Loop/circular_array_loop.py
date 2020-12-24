from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool: 
        #check for empty list
        if len(nums) == 0:
            return False      
        
        result = False

        for i in range(len(nums)):
            slow, fast = i, i
        
            while True:
                slow = self.calculate_next(nums, slow)
                fast = self.calculate_next(nums, fast)
                fast = self.calculate_next(nums, fast)
                if slow == fast:
                    break
        
            start = slow 
            curr = slow
            slow = self.calculate_next(nums, slow)     
            if slow == start:
                #Cycle is shorter than one
                continue 
            result = True
            while start != slow:
                if bool(nums[curr] > 0) != bool(nums[slow] > 0):
                    result = False
                    break
                curr = slow
                slow = self.calculate_next(nums, slow)            
        
        return result
    
    def calculate_next(self, nums, index):
        length = len(nums)
        index = (index + nums[index])
        
        return index % length