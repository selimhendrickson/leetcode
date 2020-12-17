import unittest
from duplicate_zeros import Solution

class TestDriver(unittest.TestCase):
    
    def  test_sample_1(self):
        solution = Solution()
        arr = [1,0,2,3,0,4,5,0]
        solution.duplicateZeros(arr)

        self.assertEqual(arr, [1,0,0,2,3,0,0,4])


    def  test_sample_2(self):
        solution = Solution()
        arr = [1,2,3]
        solution.duplicateZeros(arr)

        self.assertEqual(arr, [1,2,3])

if __name__ == '__main__':
    unittest.main()
