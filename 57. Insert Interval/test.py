import unittest
from insert_interval import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(Solution().insert([[1,3],[6,9]],[2,5]), [[1,5],[6,9]])

    def test_sample_2(self):
        self.assertEqual(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]), [[1,2],[3,10],[12,16]])

    def test_sample_3(self):
        self.assertEqual(Solution().insert([],[5,7]),[[5,7]])

    def test_sample_4(self):
        self.assertEqual(Solution().insert([[1,5]],[2,3]),[[1,5]])

    def test_sample_5(self):
        self.assertEqual(Solution().insert([[1,5]],[2,7]),[[1,7]])

    def test_75(self):
        self.assertEqual(Solution().insert([[1,5]],[5,7]),[[1,7]])

    def test_98(self):
        self.assertEqual(Solution().insert([[1,5]],[6,8]),[[1,5],[6,8]])

    def test_129(self):
        self.assertEqual(Solution().insert([[1,5]],[0,3]),[[0,5]])

if __name__ == "__main__":
    unittest.main()