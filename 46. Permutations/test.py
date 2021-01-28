import unittest
from permutations import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertCountEqual(Solution().permute([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

    def test_sample_2(self):
        self.assertCountEqual(Solution().permute([0,1]), [[0,1],[1,0]])

    def test_sample_3(self):
        self.assertCountEqual(Solution().permute([1]), [[1]])

if __name__ == "__main__":
    unittest.main()