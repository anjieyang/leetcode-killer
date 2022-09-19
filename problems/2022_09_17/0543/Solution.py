# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = -1
        self.getLength(root)
        return self.longest

    def getLength(self, root):
        if not root:
            return -1

        left = self.getLength(root.left)
        right = self.getLength(root.right)

        self.longest = max(self.longest, 2 + left + right)

        return 1 + max(left, right)
