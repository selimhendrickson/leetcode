import unittest
from find_the_duplicate_number import Solution

class TestDriver(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(Solution().findDuplicate([1,3,4,2,2]), 2)    

    def test_example_2(self):
        self.assertEqual(Solution().findDuplicate([3,1,3,4,2]), 3)    

    def test_example_3(self):
        self.assertEqual(Solution().findDuplicate([1,1]), 1)    

    def test_example_4(self):
        self.assertEqual(Solution().findDuplicate([1,1,2]), 1)    
        
if __name__ == "__main__":
    unittest.main()