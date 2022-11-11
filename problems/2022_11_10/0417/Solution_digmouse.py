class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return None

        M, N = len(heights[0]), len(heights)

        go_pacific = []
        go_atlantic = []

        for i in range(M):
            self._dfs(heights, i, 0, -1, go_pacific)
            self._dfs(heights, i, N - 1, -1, go_atlantic)

        for i in range(N):
            self._dfs(heights, 0, i, -1, go_pacific)
            self._dfs(heights, M - 1, i, -1, go_atlantic)

        res = []
        for i in range(N):
            for j in range(M):
                if ([i, j] in go_pacific and [i, j] in go_atlantic):
                    res.append([i, j])
        
        return res
    
    def _dfs(self, heights, i, j, height, reachable_sea):
        if i < 0 or j < 0 or i == len(heights[0]) or j == len(heights):
            return
        
        if [j, i] in reachable_sea or heights[j][i] < height:
            return

        reachable_sea.append([j, i])
        self._dfs(heights, i + 1, j, heights[j][i], reachable_sea)
        self._dfs(heights, i - 1, j, heights[j][i], reachable_sea)
        self._dfs(heights, i, j + 1, heights[j][i], reachable_sea)
        self._dfs(heights, i, j - 1, heights[j][i], reachable_sea)
