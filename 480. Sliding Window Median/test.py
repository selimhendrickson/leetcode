import unittest
from sliding_window_median import Solution

class TestDriver(unittest.TestCase):

    def test_sample_3(self):
        input = [1,3,-1,-3,5,3,6,7]
        k = 3
        self.assertEquals(Solution().medianSlidingWindow(input,k),[1,-1,-1,3,5,6])


    def test_7(self):
        input = [2147483647,1,2,3,4,5,6,7,2147483647]
        k = 2
        self.assertEquals(Solution().medianSlidingWindow(input,k),[1073741824.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1073741827.0])

if __name__ == "__main__":
    unittest.main()