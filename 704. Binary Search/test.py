import unittest
from binary_search import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEquals(Solution().search([-1,0,3,5,9,12], 9), 4)

    def test_sample_2(self):
        self.assertEquals(Solution().search([-1,0,3,5,9,12], 2), -1)        

    def test_self_1(self):
        self.assertEquals(Solution().search([-1,0,3,5,9,12], 12), 5)     

    def test_self_2(self):
        self.assertEquals(Solution().search([-1,0,3,5,9,12], 15), -1)     

if __name__ == "__main__":
    unittest.main()