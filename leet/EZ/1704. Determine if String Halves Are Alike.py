class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        slen = (int)(len(s)/2)
        helf1 = s[:slen]
        helf2 = s[slen:]
        counter1 = 0
        counter2 = 0
        for i in range(slen):
            if helf1[i] in vowels:
                counter1 += 1
            if helf2[i] in vowels:
                counter2 += 1
        return counter2 == counter1

print(Solution.halvesAreAlike(Solution,"textbook"))
