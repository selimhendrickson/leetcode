import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.globalMaximumSum = -math.inf
        self.find_maximum_path_sum_recursive(root)        
        return self.globalMaximumSum

    def find_maximum_path_sum_recursive(self, node):        
        if not node: return 0
        left_max = self.find_maximum_path_sum_recursive(node.left)
        left_max = max(left_max, 0)
        right_max = self.find_maximum_path_sum_recursive(node.right)
        right_max = max(right_max, 0)

        
        self.globalMaximumSum = max(self.globalMaximumSum, left_max + right_max + node.val)
        return max(left_max, right_max) + node.val        