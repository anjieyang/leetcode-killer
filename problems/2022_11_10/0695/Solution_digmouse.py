class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.curr_area = 0
                    self._dfs(i, j, grid)

                    max_area = max(max_area, self.curr_area)
        
        return max_area
    
    def _dfs(self, i, j, grid):
        self.curr_area += 1
        grid[i][j] = '#'

        if i - 1 >= 0 and grid[i-1][j] == 1:
            self._dfs(i - 1, j, grid)

        if i + 1 < len(grid) and grid[i+1][j] == 1:
            self._dfs(i + 1, j, grid)

        if j - 1 >= 0 and grid[i][j-1] == 1:
            self._dfs(i, j - 1, grid)

        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            self._dfs(i, j + 1, grid)