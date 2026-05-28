class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
    
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row/col as flags for the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # flag the row
                    matrix[0][j] = 0  # flag the col

        # Zero out cells based on flags (skip first row/col for now)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row and col last, using the booleans
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0