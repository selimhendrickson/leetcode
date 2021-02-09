import unittest
from Solution import KthLargest

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])

        self.assertEquals(kthLargest.add(3), 4)
        self.assertEquals(kthLargest.add(5), 5)
        self.assertEquals(kthLargest.add(10), 5)
        self.assertEquals(kthLargest.add(9), 8)
        self.assertEquals(kthLargest.add(4), 8)

    def test_1(self):
        kthLargest = KthLargest(1, [])

        self.assertEquals(kthLargest.add(-3), -3)
        self.assertEquals(kthLargest.add(-2), -2)
        self.assertEquals(kthLargest.add(-4), -2)
        self.assertEquals(kthLargest.add(0), 0)
        self.assertEquals(kthLargest.add(4), 4)        

if __name__ == "__main__":
    unittest.main()