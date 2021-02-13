import unittest
from Solution import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEquals(Solution().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]), [20, 24])

if __name__ == "__main__":
    unittest.main()