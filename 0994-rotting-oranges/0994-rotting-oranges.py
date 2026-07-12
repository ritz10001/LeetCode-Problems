from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        time = 0
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        queue = deque([])
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: # rotten orange
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0:
            rotten_oranges = len(queue)
            infected = False
            for i in range(rotten_oranges):
                r, c = queue.popleft()
                for dr, dc in directions:
                    R = r + dr
                    C = c + dc
                    if 0 <= R < rows and 0 <= C < cols and grid[R][C] == 1:
                        grid[R][C] = 2 # mark as rotten
                        queue.append((R,C))
                        fresh_oranges -= 1
            time += 1

        
        if fresh_oranges == 0:
            return time
        return -1
    
        