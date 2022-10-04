class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        row, col = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            queue = []
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue.append([r, c])

            while queue:
                currRow, currCol = queue.pop(0)
                for d in directions:
                    r, c = currRow + d[0], currCol + d[1]
                    if r in range(row) and c in range(col) and grid[r][c] == '1' and (r, c) not in visited:
                        queue.append([r, c])
                        visited.add((r, c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
