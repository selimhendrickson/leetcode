import unittest
from remove_element import Solution

class TestDriver(unittest.TestCase):
    
    def  test_1(self):
        solution = Solution()
        result = solution.removeElement([1,0,1,1,0,1])

        self.assertEqual(result, 2)


    def  test_9(self):
        solution = Solution()
        result = solution.findMaxConsecutiveOnes([1])

        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
