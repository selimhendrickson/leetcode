from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if root is None: return depth
        queue  = deque()
        queue.append(root)

        while queue:
            length = len(queue)
            depth += 1

            for _ in range(length):
                node = queue.popleft()
    
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)
                if node.left is None and node.right is None: return depth

        return depth        