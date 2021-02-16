import unittest
from Solution import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEquals(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)

    def test_sample_3(self):
        self.assertEquals(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False)

if __name__ == "__main__":
    unittest.main()