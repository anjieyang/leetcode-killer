class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.backtracking(nums, [], 0)

        return self.res

    def backtracking(self, nums, curr, i):
        if i == len(nums) and curr not in self.res:
            self.res.append(curr.copy())
            return

        if i >= len(nums):
            return

        curr.append(nums[i])
        self.backtracking(nums, curr, i + 1)

        curr.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.backtracking(nums, curr, i + 1)
