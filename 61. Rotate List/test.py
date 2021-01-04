import unittest
from rotate_list import Solution, ListNode

class TestDriver(unittest.TestCase):
    def build_linked_list(self, values):
        head = None        
        curr = None

        if len(values) > 0:
            head = ListNode(values[0])
            curr = head

        for i in range(len(values)-1):
            node = ListNode(values[i+1])
            curr.next = node
            curr = node
        
        return head
    
    def build_list(self, node):
        values = []

        while node:
            values.append(node.val)
            node = node.next

        return values
    
    def test_sample_1(self):
        input = [1,2,3,4,5]
        expected = [4,5,1,2,3]
        head = self.build_linked_list(input)      
        head = Solution().rotateRight(head, 2)
        result = self.build_list(head)

        self.assertEqual(result, expected)

    def test_sample_2(self):
        input = [0,1,2]
        expected = [2,0,1]
        head = self.build_linked_list(input)      
        head = Solution().rotateRight(head, 4)
        result = self.build_list(head)

        self.assertEqual(result, expected)

    def test_2(self):
        input = []
        expected = []
        head = self.build_linked_list(input)      
        head = Solution().rotateRight(head, 0)
        result = self.build_list(head)

        self.assertEqual(result, expected)

    def test_26(self):
        input = [1,2]
        expected = [2,1]
        head = self.build_linked_list(input)      
        head = Solution().rotateRight(head, 1)
        result = self.build_list(head)

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()