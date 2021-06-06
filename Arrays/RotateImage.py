class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        i = j = 0
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        i = j = 0
        for i in range(rows):
            for j in range(cols // 2):
                matrix[i][j], matrix[i][cols - j - 1] = \
                    matrix[i][cols - j - 1], matrix[i][j]