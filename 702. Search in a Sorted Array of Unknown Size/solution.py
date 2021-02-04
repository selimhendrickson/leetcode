# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, key):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        bounds = 4

        # find the range where the key is
        while reader.get(right) != 2147483647:
            if key >= reader.get(left) and key <= reader.get(right): break
            left = right + 1
            right += bounds
            bounds = bounds * 2

        # now that we have the range, search for the key using binary search
        # right end of the range can be out of bounds. We'll care for that later. 

        while left <= right:
            mid = left + (right - left) // 2
            if reader.get(mid) == key: return mid
            if reader.get(mid) < key:
                left = mid + 1
            else:
                right = mid - 1
                  
        return -1        
        