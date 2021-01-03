import unittest
from reverse_linked_list_II import Solution, ListNode

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
        expected = [1,4,3,2,5]
        head = self.build_linked_list(input)      
        Solution().reverseBetween(head, 2, 4)
        result = self.build_list(head)

        self.assertEqual(result, expected)

    def test_1(self):
        input = [5]
        expected = [5]
        head = self.build_linked_list(input)      
        Solution().reverseBetween(head, 1, 1)
        result = self.build_list(head)

        self.assertEqual(result, expected)

    def test_2(self):
        input = [3,5]
        expected = [5,3]
        head = self.build_linked_list(input)      
        head = Solution().reverseBetween(head, 1, 2)
        result = self.build_list(head)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
