# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.left = self.preOrder(p, [])
        self.right = self.preOrder(q, [])

        return self.left == self.right

    def preOrder(self, tree, curr):
        if not tree:
            curr.append('null')
            return
        curr.append(tree.val)
        self.preOrder(tree.left, curr)
        self.preOrder(tree.right, curr)

        return curr
