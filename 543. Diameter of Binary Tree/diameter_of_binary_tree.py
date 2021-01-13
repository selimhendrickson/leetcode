# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.treeDiameter = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, node):    
        if node is None: return 0
        left_height, right_height = 0, 0
    
        if node.left:
            left_height += 1
            left_height += self.calculate_height(node.left)
        if node.right:
            right_height += 1
            right_height += self.calculate_height(node.right)

        # see if we found a new max
        self.treeDiameter = max(self.treeDiameter, left_height + right_height)
        return max(left_height, right_height)        