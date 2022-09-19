# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, root, left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False

        leftTree = self.checkBST(root.left, left, root.val)
        rightTree = self.checkBST(root.right, root.val, right)

        return leftTree and rightTree
