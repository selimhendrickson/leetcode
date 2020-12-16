import unittest
from find_numbers_with_even_number_of_digits import Solution

class TestDriver(unittest.TestCase):
    
    def  test_sample_1(self):
        solution = Solution()
        result = solution.findNumbers([12,345,2,6,7896])

        self.assertEqual(result, 2)


    def  test_sample_2(self):
        solution = Solution()
        result = solution.findNumbers([555,901,482,1771])

        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
