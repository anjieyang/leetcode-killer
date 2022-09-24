class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedIdx = []
        for i in range(len(nums)):
            sortedIdx.append([nums[i], i])
        sortedIdx.sort()

        start, end = 0, len(sortedIdx) - 1

        while start < end:
            total = sortedIdx[start][0] + sortedIdx[end][0]
            if total == target:
                return [sortedIdx[start][1], sortedIdx[end][1]]
            elif total < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]
