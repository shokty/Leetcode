class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_new = ""
        T_new = ""
        for char in S:
            if char == '#':
                S_new = S_new[:-1]
            else:
                S_new += char
        for char in T:
            if char == '#':
                T_new = T_new[:-1]
            else:
                T_new += char
        return S_new == T_new
