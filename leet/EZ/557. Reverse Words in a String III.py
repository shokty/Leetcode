class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string_plited = s.split(" ")
        answear = ""
        for i in range(len(string_plited)):
            answear += string_plited[i][::-1]
            if (i != len(string_plited) - 1):
                answear += " "
        return answear

print(Solution.reverseWords(Solution,"Let's take LeetCode contest"))