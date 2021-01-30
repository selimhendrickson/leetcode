import unittest
from solution import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEquals(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8), [3, 4])

    def test_sample_2(self):
        self.assertEquals(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6), [-1, -1])

    def test_sample_3(self):
        self.assertEquals(Solution().searchRange(nums = [], target = 0), [-1, -1])

    def test_sample_62(self):
        self.assertEquals(Solution().searchRange(nums = [0,0,1,2,2], target = 0), [0, 1])

    def test_sample_69(self):
        self.assertEquals(Solution().searchRange(nums = [0,0,1,1,2,2,2,2,3,3,4,4,4,5,6,6,6,7,8,8], target = 4), [10, 12])

if __name__ == "__main__":
    unittest.main()