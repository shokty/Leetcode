class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = "".join(sorted(s1))
        s2 = "".join(sorted(s2))
        continu1 = True
        continu2 = True
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                continu1 = False
            elif s2[i] > s1[i]:
                continu2 = False
        return continu2 or continu1

print(Solution.checkIfCanBreak(Solution,"szy"
,"cid"))