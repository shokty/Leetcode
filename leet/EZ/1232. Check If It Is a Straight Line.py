class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        y2 = coordinates[1][1]
        y1 = coordinates[0][1]
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        for (x,y) in coordinates:
            if  (x-x1)*(y2-y1) != (y-y1)*(x2-x1):
                return False
        return True