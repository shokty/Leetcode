class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        answear = ""
        for i in range(len(command)):
            if command[i] == 'G':
                answear += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    answear += 'o'
                    i += 1
                else:
                    answear+= 'al'
                    i += 2
        return answear

print(Solution.interpret(Solution,"G()()()()(al)"))
