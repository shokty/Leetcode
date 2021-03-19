class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        answear = [ [1]
                   ]
        for i in range(1,numRows):
            lates_row = len(answear) -1
            lates_row_len = len(answear[lates_row])
            newrow = [1]*(lates_row_len+1)
            for i in range(0,lates_row_len-1):
                newrow[i+1] = answear[lates_row][i] + answear[lates_row][i+1]
            answear.append(newrow)
        return answear


print(Solution.generate(Solution,5))