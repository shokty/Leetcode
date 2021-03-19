class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dicty = {}
        newone = True
        for i in range(len(S)):
            if S[i] in dicty:
                dicty[S[i]][1] = i
            else:
                dicty[S[i]] = [i,i]

        answear = [dicty[S[0]][1]]
        splits = 0
        for i in range(len(S)):
            currchar = S[i]
            if (dicty[currchar][0] > answear[splits]):
                answear.append(dicty[currchar][1])
                splits +=1
            elif dicty[currchar][1] > answear[splits]:
                answear[splits] = dicty[currchar][1]

        sum = -1
        for i in range(len(answear)):
            answear[i] -= sum
            sum += answear[i]
        return answear

print(Solution.partitionLabels(Solution,"ababcbacadefegdehijhklij"))


