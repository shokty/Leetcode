def can_get_out(grid):
    N = len(grid)
    soul = [[ 0 for j in range(N) ] for i in range(N) ]

    def isSafe(maze, x, y):
        return grid[x][y] == 1 if (0 <= x < N and 0 <= y < N) else False

    def find_soul(x, y,soul):
        if isSafe(grid,x, y):
            if (soul[x][y] == 1):
                return False
            if x == N - 1 and y == N - 1:
                soul[x][y] = 1
                return True
            soul[x][y] = 1
            if find_soul(x+1, y,soul) or find_soul(x,y+1,soul) or find_soul(x-1,y,soul) or find_soul(x,y+1,soul):
                return True
            soul[x][y] = 0
        return False

    if find_soul(0, 0,soul):
        print(soul)
        return True
    return False


gridy = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
print(can_get_out(gridy))
