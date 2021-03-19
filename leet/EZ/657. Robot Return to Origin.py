class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for move in moves:
            if move == 'u' or move == 'U':
                y +=1
            elif move == 'd' or move == 'D':
                y -=1
            elif move == 'R' or move == 'r':
                x += 1
            elif move == 'l' or move == 'L':
                x -= 1
        return x == y == 0
