import unittest
from squares_of_a_sorted_array import Solution

class TestDriver(unittest.TestCase):
    
    def  test_sample_1(self):
        solution = Solution()
        result = solution.sortedSquares([-4,-1,0,3,10])

        self.assertEqual(result, [0,1,9,16,100])

    def  test_sample_2(self):
        solution = Solution()
        result = solution.sortedSquares([-7,-3,2,3,11])

        self.assertEqual(result, [4,9,9,49,121])

if __name__ == '__main__':
    unittest.main()
