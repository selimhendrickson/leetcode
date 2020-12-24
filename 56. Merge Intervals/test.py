import unittest
from merge_intervals import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(Solution().merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

    def test_sample_2(self):
        self.assertEqual(Solution().merge([[1,4],[4,5]]),[[1,5]])
        
if __name__ == "__main__":
    unittest.main()