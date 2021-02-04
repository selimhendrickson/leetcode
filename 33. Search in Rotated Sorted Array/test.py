import unittest
from solution import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(Solution().search([4,5,6,7,0,1,2],0), 4)

    def test_1(self):
        self.assertEqual(Solution().search([4,5,6,7,0,1,2],3), -1)

    def test_168(self):
        self.assertEqual(Solution().search([1,3],1), 0)
    
    def test_170(self):
        self.assertEqual(Solution().search([1,3],3), 1)

    def test_181(self):
        self.assertEqual(Solution().search([3,1],3), 0)

    def test_186(self):
        self.assertEqual(Solution().search([5,1,3],5), 0)        

    def test_191(self):
        self.assertEqual(Solution().search([6,7,8,1,2,3,4,5],6), 0)

    def test_193(self):
        self.assertEqual(Solution().search([4,5,6,7,8,1,2,3],8), 4)   

if __name__ == "__main__":
    unittest.main()