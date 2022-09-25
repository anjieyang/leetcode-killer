class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [], 0)
        return self.res
    
    def dfs(self, nums, curr, index):
        if index >= len(nums):
            self.res.append(curr.copy())
            return
        
        # decision to include current index
        curr.append(nums[index])
        self.dfs(nums, curr, index + 1)
        
        # decision not to include current index
        curr.pop()
        self.dfs(nums, curr, index + 1)