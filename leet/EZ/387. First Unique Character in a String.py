import queue


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicty = {}
        dontteach = set()
        for i in range(len(s)):
            char = s[i]
            if char in dicty:
                dicty.pop(char)
                dontteach.add(char)
            elif char not in dontteach:
                dicty[char] = i
        min = 100000000000
        for key in dicty:
            if dicty[key] < min:
                min = dicty[key]
        if min != 100000000000:
            return min
        return -1

Solution.firstUniqChar(Solution,"leetcode")
