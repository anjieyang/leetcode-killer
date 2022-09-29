class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.length = len(nums)
        self.backtracking(nums, [])

        return self.res

    def backtracking(self, nums, curr):
        if len(curr) == self.length:
            self.res.append(curr.copy())
            return

        for i in range(len(nums)):
            self.backtracking(nums[0:i] + nums[i+1:], curr + [nums[i]])
