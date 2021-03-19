class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        mem = set()
        while n != '1':
            list_of_n = [int(x) for x in str(n)]
            n = 0
            for i in range(len(list_of_n)):
                n+= pow(list_of_n[i],2)
            n = str(n)
            if n in mem:
                return False
            else:
                mem.add(n)
        return True

print(Solution.isHappy(Solution,19))