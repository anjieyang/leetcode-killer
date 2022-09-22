class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        if len(nums) < 3:
            return res

        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1

                else:
                    right -= 1

        return [list(x) for x in res]
