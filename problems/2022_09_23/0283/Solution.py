class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, res = 1, 1, [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res
