# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        self.dfs(root, root.val)
        return self.count

    def dfs(self, root, curMax):
        if not root:
            return

        if (root.val >= curMax):
            self.count += 1

        curMax = max(root.val, curMax)
        self.dfs(root.left, curMax)
        self.dfs(root.right, curMax)
