class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        points.sort(key=lambda x:x[1])
        arrowpos = points[0][1]
        arrowcount = 1
        for point in points:
            if point[0] <= arrowpos:
                continue
            arrowcount +=1
            arrowpos = point[1]
        return arrowcount

print(Solution.findMinArrowShots(Solution,[[10,16],[2,8],[1,6],[7,12]]))