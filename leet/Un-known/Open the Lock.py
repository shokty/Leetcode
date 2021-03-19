import queue


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        wherecan_i_go = {'0': ['9', '1'], '1': ['0', '2'], '2': ['1', '3'], '3': ['2', '4'], '4': ['3', '5']
            , '5': ['4', '6'], '6': ['5', '7'], '7': ['6', '8'], '8': ['7', '9'], '9': ['8', '0']}
        S = set()
        Deadendset = set()
        for deadend in deadends:
            Deadendset.add(deadend)
        Q = queue.Queue()
        Q.put("0000")
        if ("0000" in deadends):
            return -1

        def helper(steps):
            while Q.qsize() != 0:
                size = Q.qsize()
                while size > 0:
                    mytry = Q.get()

                    if (mytry == target):
                        return steps

                    for i in range(0, 4):
                            S.add(mytry)
                            s1 = mytry[0:i] + wherecan_i_go[mytry[i]][0] + mytry[i + 1:]
                            s2 = mytry[0:i] + wherecan_i_go[mytry[i]][1] + mytry[i + 1:]
                            if s1 not in Deadendset and s1 not in S:
                                S.add(s1)
                                Q.put(s1)
                            if s2 not in Deadendset and s2 not in S:
                                S.add(s2)
                                Q.put(s2)

                    size -= 1
                steps += 1
            return -1

        return helper(0)


deadends = []
target = "8888"
print(Solution.openLock(Solution, deadends, target))
