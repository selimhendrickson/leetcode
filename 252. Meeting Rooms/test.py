import unittest
from meeting_rooms import Solution

class TestDriver(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]), False)

    def test_sample_2(self):
        self.assertEqual(Solution().canAttendMeetings([[7,10],[2,4]]), True)

if __name__ == "__main__":
    unittest.main()