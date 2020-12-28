import unittest
from interval_list_intersections import Solution

class TestDriver(unittest.TestCase):

    def test_example_1(self):
        A = [[1, 3], [5, 6], [7, 9]]
        B = [[2, 3], [5, 7]]
        output = [[2, 3], [5, 6], [7, 7]]
        self.assertEqual(Solution().intervalIntersection(A,B),output)

    def test_example_2(self):
        A = [[1, 3], [5, 7], [9, 12]]
        B = [[5, 10]]
        output = [[5, 7], [9, 10]]
        self.assertEqual(Solution().intervalIntersection(A,B),output)

    def test_sample_1(self):
        A = [[0,2],[5,10],[13,23],[24,25]]
        B = [[1,5],[8,12],[15,24],[25,26]]
        output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        self.assertEqual(Solution().intervalIntersection(A,B),output)

if __name__ == "__main__":
    unittest.main()
        