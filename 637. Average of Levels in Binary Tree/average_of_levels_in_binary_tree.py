from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if root is None: return result

        queue = deque()
        queue.append(root)
  
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()      

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level.append(node.val)

            result.append(sum(level)/len(level))

        return result        