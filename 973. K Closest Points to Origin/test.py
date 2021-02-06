import unittest
from solution import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEquals(Solution().kClosest([[1,3],[-2,2]], 1), [[-2,2]] )

if __name__ == "__main__":
    unittest.main()