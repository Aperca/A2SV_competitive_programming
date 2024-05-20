class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ans = [([0] * (n - 2)) for i in range(n - 2)]

        for x in range(n - 2):
            for y in range(n - 2):
                curr_max = 0
                for r in range(x, x + 3):
                    for c in range(y, y + 3):
                        curr_max = max(curr_max, grid[r][c])
                ans[x][y] = curr_max

        return ans
