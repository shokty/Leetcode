class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        stringdict = {}
        answear  = ""
        notindict = ""
        for i in range (len(S)):
            stringdict[S[i]] = 0
        for char in T:
            if char in stringdict:
                stringdict[char] += 1
            else:
                notindict += char
        for char in S:
            answear += char * stringdict[char]
        return answear + notindict

S = "cba"
T = "abcdaaaaaaaa"
print(Solution.customSortString(Solution,S,T))