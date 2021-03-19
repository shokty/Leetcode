import string


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        answer = [S]
        def healper(S,index):
            if index >= len(S):
                return ;
            cur = S[index]
            if 'a' <= cur <= 'z':
                stemp = S[0:index] + cur.upper() + S[index+1:]
                answer.append(stemp)
                healper(stemp,index+1)
            elif 'A' <= cur <= 'Z':
                stemp = S[0:index] + cur.lower() + S[index+1:]
                answer.append(stemp)
                healper(stemp,index+1)
            healper(S, index + 1)

        healper(S,0)
        return answer

print(Solution.letterCasePermutation(Solution,"a1b2"))