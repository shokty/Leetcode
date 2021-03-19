class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        coulms = len(image[0])
        visited = [[0 for i in range(coulms)] for j in range(rows)]
        def dfs(grid, i, j, colortochange, newColor):
            if (i < 0 or j < 0 or i >= rows or j >= coulms or grid[i][j] != colortochange or visited[i][j] == 1):
                return;
            visited[i][j] = 1
            grid[i][j] = newColor
            dfs(grid, i - 1, j, colortochange, newColor)
            dfs(grid, i + 1, j, colortochange, newColor)
            dfs(grid, i, j - 1, colortochange, newColor)
            dfs(grid, i, j + 1, colortochange, newColor)
        dfs(image,sr,sc,image[sr][sc],newColor)
        return image

image = [[0,0,0],[0,1,1]]
print(Solution.floodFill(Solution,image,1,1,1))