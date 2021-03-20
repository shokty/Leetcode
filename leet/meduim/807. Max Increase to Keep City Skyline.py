class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows_max = []
        coulms_max = []
        def find_max_in_coulm(index,len):
            maxi = 0
            for i in range(len):
                maxi = max(grid[i][index],maxi)
            return maxi
        for i in range(len(grid)):
            rows_max.append(max(grid[i]))

        for i in range(len(grid[0])):
            coulms_max.append(find_max_in_coulm(i,len(grid)))
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                sum += min(rows_max[i],coulms_max[j]) - grid[i][j]

        return sum

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(Solution.maxIncreaseKeepingSkyline(Solution,grid))