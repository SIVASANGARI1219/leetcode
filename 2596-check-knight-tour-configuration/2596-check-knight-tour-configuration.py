class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        # Step 1: must start at (0,0)
        if grid[0][0] != 0:
            return False

        # Step 2: store positions of each number
        pos = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)

        # Step 3: check all moves
        for k in range(n * n - 1):
            r1, c1 = pos[k]
            r2, c2 = pos[k + 1]

            dx = abs(r1 - r2)
            dy = abs(c1 - c2)

            if not ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
                return False

        return True