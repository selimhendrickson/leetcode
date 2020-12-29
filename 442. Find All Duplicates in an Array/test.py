import unittest
from find_all_duplicates_in_an_array import Solution

class TestDriver(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(Solution().findDuplicates([4,3,2,7,8,2,3,1]), [2,3])    

if __name__ == "__main__":
    unittest.main()