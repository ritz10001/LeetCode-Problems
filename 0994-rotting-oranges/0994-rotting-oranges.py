from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        minutes = 0
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                else:
                    continue
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0<=r<rows and 0<=c<cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))
                        fresh -= 1
            minutes += 1
        if fresh > 0:
            return -1
        return minutes
        