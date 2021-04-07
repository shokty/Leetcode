class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k = ""
        s = s.lower()
        for char in s:
            if 'a' <= char <= 'z':
                k += char
        start = 0
        end = len(k) - 1
        while start < end:
            if k[start] != k[end]:
                return False
            start += 1
            end   -= 1
        return True

print(Solution.isPalindrome(Solution,s = "A man, a plan, a canal: Panama"))