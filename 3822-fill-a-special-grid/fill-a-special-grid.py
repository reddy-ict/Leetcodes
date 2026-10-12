class Solution(object):
    def specialGrid(self, n):
        size = 2 ** n
        grid = [[0] * size for _ in range(size)]
        count = [0]

        def fill(r, c, length):
            if length == 1:
                grid[r][c] = count[0]
                count[0] += 1
                return

            half = length // 2

            # Top-right
            fill(r, c + half, half)

            # Bottom-right
            fill(r + half, c + half, half)

            # Bottom-left
            fill(r + half, c, half)

            # Top-left
            fill(r, c, half)

        fill(0, 0, size)
        return grid
