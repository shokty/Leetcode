class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """

        sorted_list = sorted(text.split(" "), key=len)
        return " ".join(sorted_list).lower().capitalize()

print(Solution.arrangeWords(Solution,"Leetcode is cool"))