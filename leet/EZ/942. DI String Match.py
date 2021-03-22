class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        D = len(S)
        I = 0
        answear = []
        for char in S:
            if char == 'D':
                answear.append(D)
                D -= 1
            if char == 'I':
                answear.append(I)
                I +=1
        if answear[-1] == D:
            answear.append(I)
        else:
            answear.append(D)
        return answear
