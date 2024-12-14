class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        def bfs(r,c):
            offsets = [(1,0), (0,1), (-1,0), (0,-1)]
            queue = []
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                row, col = queue.pop(0)
                for nr, nc in offsets:
                    r = row + nr
                    c = col + nc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    print("r,c", (r,c))
                    bfs(r,c)
                    islands += 1
        return islands
        