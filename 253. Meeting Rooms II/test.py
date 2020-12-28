import unittest
from meeting_rooms_II import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]), 2)

    def test_sample_2(self):
        self.assertEqual(Solution().minMeetingRooms([[7,10],[2,4]]), 1)

    def test_example_1(self):
        self.assertEqual(Solution().minMeetingRooms([[1,4], [2,5], [7,9]]), 2)

    def test_example_2(self):
        self.assertEqual(Solution().minMeetingRooms([[6,7], [2,4], [8,12]]), 1)

    def test_example_3(self):
        self.assertEqual(Solution().minMeetingRooms([[1,4], [2,3], [3,6]]), 2)

    def test_example_4(self):
        self.assertEqual(Solution().minMeetingRooms([[4,5], [2,3], [2,4], [3,5]]), 2)


if __name__ == "__main__":
    unittest.main()