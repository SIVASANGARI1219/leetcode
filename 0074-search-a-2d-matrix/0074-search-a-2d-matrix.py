class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for k in range(m * n):
            if matrix[k // n][k % n] == target:
                return True
        return False
        