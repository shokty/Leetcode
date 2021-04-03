class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        a_to_z = []
        digits = []
        for char in s:
            if 'a' <= char <= 'z':
                a_to_z.append(char)
            else:
                digits.append(char)
        answear = ""
        if abs(len(a_to_z) - len(digits)) <= 1:
            while a_to_z != [] and digits != []:
                answear += a_to_z.pop()
                answear += digits.pop()
            if a_to_z != []:
                answear = a_to_z.pop() + answear
            elif digits != []:
                answear += digits.pop()
        return answear

print(Solution.reformat(Solution,"a0b1c2"))