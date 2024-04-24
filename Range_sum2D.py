class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.presum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            prefix = 0 
            for c in range(cols):
                prefix += matrix[r][c] 
                above = self.presum[r][c + 1]
                self.presum[r + 1][c + 1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1

        bottomRight = self.presum[r2][c2]
        above = self.presum[r1 - 1][c2]
        left = self.presum[r2][c1 - 1]
        topLeft = self.presum[r1 - 1][c1 - 1]  

        return bottomRight - above - left + topLeft
