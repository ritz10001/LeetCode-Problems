from collections import deque
class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = set()
        islands = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r,c) not in visited):
                return 0
            visited.add((r, c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

            return 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += dfs(r, c)
        return islands
        