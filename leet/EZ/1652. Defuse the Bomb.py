class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        code_len = len(code)
        res = []
        for i in range(code_len):
            sumy = 0
            for j in range(abs(k)):
                if k > 0:
                    where_to_go = (i + k - j) % code_len
                else:
                    where_to_go = (i + k + j) % code_len
                sumy += code[where_to_go]
            res.append(sumy)
        return res

print(Solution.decrypt(Solution,[2,4,9,3],-2))
