class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def chack_if_winner(grid,x,y):
            if sum(grid[x]) == 0 or (grid[0][y] + grid[1][y] + grid[2][y]) == 0\
                    or grid[0][0] + grid[1][1] + grid[2][2] == 0 or grid[2][0] + grid[1][1] + grid[0][2] == 0:
                return 'A'
            elif sum(grid[x]) == 3 or (grid[0][y] + grid[1][y] + grid[2][y]) == 3 \
                or grid[0][0] + grid[1][1] + grid[2][2] == 3 or grid[2][0] + grid[1][1] + grid[0][2] == 3:
                return 'B'
            return None
        grid = [[-5,-5,-5],[-5,-5,-5],[-5,-5,-5]]
        who_turn = 0
        for (x,y) in moves:
            grid[x][y] = who_turn%2
            rv = chack_if_winner(grid,x,y)
            if rv:
                return rv
            who_turn +=1
        if who_turn == 9:
            return "Draw"
        else:
            return "Pending"


print(Solution.tictactoe(Solution,
[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]  ))