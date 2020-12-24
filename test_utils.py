class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_linked_list(values):
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

def build_list(node):
    values = []

    while node:
        values.append(node.val)
        node = node.next

    return values