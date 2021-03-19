class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def clean(grid, i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0):
                return;
            grid[i][j] = 0
            clean(grid, i - 1, j)
            clean(grid, i + 1, j)
            clean(grid, i, j + 1)
            clean(grid, i, j - 1)
        rows = len(A)
        if rows <=1:
            return 0
        coulm = len(A[0])
        for i in range(coulm):
            if (A[0][i] == 1):
                clean(A,0,i)
            if (A[rows-1][i] == 1):
                clean(A,rows-1,i)

        for i in range(rows):
            if A[i][0] == 1:
                clean(A, i, 0)
            if A[i][coulm-1] == 1:
                clean(A, i, coulm-1)
        counter = 0
        for i in range(rows):
            for j in range(coulm):
                counter += A[i][j]
        return counter

Input = \
[[0,0,1,1,1,0,1,1,1,0,1],
 [1,1,1,1,0,1,0,1,1,0,0],
 [0,1,0,1,1,0,0,0,0,1,0],
 [1,0,1,1,1,1,1,0,0,0,1],
 [0,0,1,0,1,1,0,0,1,0,0],
 [1,0,0,1,1,1,0,0,0,1,1],
 [0,1,0,1,1,0,0,0,1,0,0],
 [0,1,1,0,1,0,1,1,1,0,0],
 [1,1,0,1,1,1,0,0,0,0,0],
 [1,0,1,1,0,0,0,1,0,0,1]]



Input2 = [[0, 1, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]]
print(Solution.numEnclaves(Solution,Input))
print(Solution.numEnclaves(Solution,Input2))