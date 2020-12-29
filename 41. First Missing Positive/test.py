import unittest
from first_missing_positive import Solution

class TestDriver(unittest.TestCase):

    def testExample1(self):
        self.assertEqual(Solution().firstMissingPositive([1,2,0]), 3)

    def testExample2(self):
        self.assertEqual(Solution().firstMissingPositive([3,4,-1,1]), 2)

    def testExample3(self):
        self.assertEqual(Solution().firstMissingPositive([7,8,9,11,12]), 1)

if __name__ == "__main__":
    unittest.main()