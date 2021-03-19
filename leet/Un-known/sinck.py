class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if (grid[i][j] == '1'):
                    self.dfs(self,grid,i,j)
                    counter += 1
        return counter

    def dfs(self,grid,i,j):
        if (i < 0 or j < 0 or i >= (len (grid)) or j >= (len (grid[i])) or grid[i][j] == '0' ):
            return ;
        grid[i][j] = '0'
        self.dfs(self,grid, i + 1,j)
        self.dfs(self,grid, i - 1, j)
        self.dfs(self,grid, i , j + 1)
        self.dfs(self,grid, i , j - 1)

grid2 = [[1,0,0,1],
        [1,0,1,1],
        [1,0,0,0],
        [0,1,0,1]]

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
print(Solution.numIslands(Solution,grid))
