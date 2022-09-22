class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = float('-inf')

        start, end = 0, len(height) - 1

        while start < end:
            area = (end - start) * min(height[end], height[start])
            maxArea = max(maxArea, area)

            if (height[start] < height[end]):
                start += 1
            else:
                end -= 1

        return maxArea
