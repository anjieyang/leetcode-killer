# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        self.countDepth(root, 0)
        return self.maxD

    def countDepth(self, root, count):
        if not root:
            self.maxD = max(self.maxD, count)
            return
        self.countDepth(root.left, count + 1)
        self.countDepth(root.right, count + 1)
