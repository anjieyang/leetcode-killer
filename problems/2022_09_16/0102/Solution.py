# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        self.level = []
        self.queue = [root]

        while self.queue:
            queueLength = len(self.queue)
            curr = []
            for i in range(queueLength):
                node = self.queue.pop(0)
                curr.append(node.val)
                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)
            self.level.append(curr)

        return self.level
