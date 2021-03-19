class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        b = x^y
        binary = bin(b)
        setBits = [ones for ones in binary[2:] if ones=='1']
        return len(setBits)