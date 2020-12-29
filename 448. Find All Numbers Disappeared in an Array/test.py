import unittest
from find_all_numbers_disappeared_in_an_array import Solution

class TestDriver(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6])    

if __name__ == "__main__":
    unittest.main()