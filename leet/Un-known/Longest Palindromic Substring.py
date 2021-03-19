class Solution(object):
    def longestPalindrome(self, s):
        if (len(s) < 1):
            return 0
        currstring = ""
        for i in range(len(s)):
            middle = Solution.expandpalindormail(self, s, i, i)
            middleplus1 = Solution.expandpalindormail(self, s, i, i + 1)
            currstring = Solution.maxstring(self, currstring, middle, middleplus1)
        return currstring

    def expandpalindormail(self, s, left, right):

        if (left > right or s == ""):
            return 0;

        lan = len(s)
        while (left >= 0 and right < lan and s[left] == s[right]):
            left -= 1;
            right += 1
        return s[left + 1:right]

    def maxstring(self, old, middle, middleplus1):
        if (len(middle) > len(middleplus1)):
            if (len(middle) > len(old)):
                return middle

        elif (len(middleplus1) > len(old)):
            return middleplus1
        return old

print(Solution.longestPalindrome(Solution, "bab"))
