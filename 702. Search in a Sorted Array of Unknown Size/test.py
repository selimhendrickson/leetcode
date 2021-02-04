import unittest
from solution import Solution

class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return 2147483647
    return self.arr[index]

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        reader = ArrayReader([-1,0,3,5,9,12])
        self.assertEquals(Solution().search(reader, 9), 4)

    def test_sample_2(self):
        reader = ArrayReader([-1,0,3,5,9,12])
        self.assertEquals(Solution().search(reader, 2), -1)

if __name__ == "__main__":
    unittest.main()

