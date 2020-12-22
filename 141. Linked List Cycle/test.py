import unittest
from linked_list_cycle import Solution, ListNode

class TestDriver(unittest.TestCase):
    head = ListNode(1)
    head.next = ListNode(2)   
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    
    def test_sample_1(self):
        self.assertEqual(Solution().hasCycle(self.head), False)

    def test_sample_2(self):
        self.head.next.next.next.next.next.next = self.head.next.next
        self.assertEqual(Solution().hasCycle(self.head), True)

    def test_sample_3(self):
        self.head.next.next.next.next.next.next = self.head.next.next.next
        self.assertEqual(Solution().hasCycle(self.head), True)

if __name__ == '__main__':
    unittest.main()
