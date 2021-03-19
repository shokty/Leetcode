from self import self


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Solution(object):
    def rotate(self, matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(i,N):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(N):
            matrix[i].reverse()
        return matrix
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

    def swap(self, matrix, i, j, n):
        temp = matrix[n-i-1][n-j-1]
        matrix[n - i - 1][n - j - 1] = matrix[i][j]
        matrix[i][j] = temp


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(matrix)
    print(Solution.rotate(Solution,matrix))
    print_hi('PyCharm')
