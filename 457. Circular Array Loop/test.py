import unittest
from circular_array_loop import Solution

class TestDriver(unittest.TestCase):    

    def test_sample_1(self):
        input = [2,-1,1,2,2]        
        result = Solution().circularArrayLoop(input)        

        self.assertEqual(result, True)

    def test_sample_2(self):
        input = [-1,2]
        result = Solution().circularArrayLoop(input)
        
        self.assertEqual(result, False)

    def test_sample_3(self):
        input = [-2, 1, -1, -2, -2]
        result = Solution().circularArrayLoop(input)

        self.assertEqual(result, False)

    def test_sample_24(self):
        input = [3, 1, 2]
        result = Solution().circularArrayLoop(input)

        self.assertEqual(result, True)

    def test_sample_26(self):
        input = [-1, -1, 3]
        result = Solution().circularArrayLoop(input)

        self.assertEqual(result, False)

    def test_sample_32(self):
        input = [-2, -3, -9]
        result = Solution().circularArrayLoop(input)

        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()


