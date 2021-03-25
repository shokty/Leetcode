class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        chackshit = " ".join(words)
        answear = []
        for word in words:
            if chackshit.count(word) >= 2:
                answear.append(word)
        return answear