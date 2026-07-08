from collections import deque
class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque([(r,c)])
            while queue:
                R, C = queue.popleft()
                for dr, dc in directions:
                    currentR = R + dr
                    currentC = C + dc
                    if 0 <= currentR < rows and 0 <= currentC < cols and grid[currentR][currentC] == "1" and (currentR, currentC) not in visited:
                        visited.add((currentR, currentC))
                        queue.append((currentR, currentC))
            return 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += bfs(r, c)
        return islands
        