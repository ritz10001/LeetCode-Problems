"""
idea: use a DFS approach to recurse through each of the 1's. Use a visited
set to check if we have already gone through that specific 1.
"""
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        def bfs(r,c):
            queue = deque([(r,c)]) #queue((r,c)) -> [(r,c)]
            while queue:
                current_x, current_y = queue.popleft() # (r,c)
                for x, y in directions:
                    child_x = current_x + x
                    child_y = current_y + y
                    if 0 <= child_x < rows and 0 <= child_y < cols and grid[child_x][child_y] == "1" and (child_x, child_y) not in visited:
                        visited.add((child_x, child_y))
                        queue.append((child_x, child_y))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

        
        