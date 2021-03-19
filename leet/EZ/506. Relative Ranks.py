class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        dity = {}
        for i in range(len(score)):
            dity[score[i]] = i
        score.sort(reverse=True)
        answear = ["0"]*len(score)
        for i in range(len(score)):
            if (i==0):
                answear[dity[score[i]]] = "Gold Medal"
            elif (i==1):
                answear[dity[score[i]]] = "Silver Medal"
            elif (i==2):
                answear[dity[score[i]]] = "Bronze Medal"
            else:
                answear[dity[score[i]]] = str(i)
        return answear
print(Solution.findRelativeRanks(Solution,[10,3,8,9,4]))
