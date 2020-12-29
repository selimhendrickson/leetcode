import unittest
from missing_number import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(Solution().missingNumber([3,0,1]),2)

    def test_sample_2(self):
        self.assertEqual(Solution().missingNumber([0,1]),2)

    def test_sample_3(self):
        self.assertEqual(Solution().missingNumber([9,6,4,2,3,5,7,0,1]),8)

    def test_sample_4(self):
        self.assertEqual(Solution().missingNumber([0]),1)

if __name__ == "__main__":
    unittest.main()