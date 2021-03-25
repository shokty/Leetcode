class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        newarry =  sentence.split(" ")
        for i in range(len(newarry)):
            if searchWord in newarry[i] and newarry[i].index(searchWord) == 0:
                return i+1
        return -1

print(Solution.isPrefixOfWord(Solution,"i love eating burger","burg"))