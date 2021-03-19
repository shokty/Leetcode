class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        distancse_from_target = abs(target[0]) + abs(target[1]);
        for ghost in ghosts:
            if (abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])) <= distancse_from_target:
                return False

        return True