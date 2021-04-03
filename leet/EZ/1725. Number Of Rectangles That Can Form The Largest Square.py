class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        dicty = {}
        for [num1,num2] in rectangles:
            mini = min(num1,num2)
            if mini not in dicty:
                dicty[mini] = 0
            dicty[mini] += 1

        maxy_size = 0
        maxy_amount = 0
        for react_size in dicty:
            if maxy_size < react_size:
                maxy_amount = dicty[react_size]
                maxy_size = react_size
        return maxy_amount

print(Solution.countGoodRectangles(Solution,[[5,8],[3,9],[5,12],[16,5]]))
