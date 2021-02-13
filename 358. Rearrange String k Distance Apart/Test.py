import unittest
from Solution import Solution

class TestDriver(unittest.TestCase):


    def test_45(self):
        self.assertEquals(Solution().rearrangeString3("aaadbbcc",2),"abacabcd")

    def test_47(self):
        self.assertEquals(Solution().rearrangeString3("aa",0),"aa")        

if __name__ == "__main__":
    unittest.main()