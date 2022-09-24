class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, maxLen = set(nums), 0

        for i in nums:
            if (i - 1) not in numsSet:
                currLen = 1
                while i + currLen in numsSet:
                    currLen += 1
                maxLen = max(maxLen, currLen)

        return maxLen
