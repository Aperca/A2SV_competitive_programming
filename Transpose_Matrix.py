class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])  

        t = [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                t[j][i] = matrix[i][j]

        return t
