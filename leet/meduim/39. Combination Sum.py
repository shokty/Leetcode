class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted(candidates)
        answear = []
        def dfs(numbers,curr_sum,curr_list):
            if curr_sum == target:
                answear.append(curr_list)
            elif curr_sum < target:
                for i in range(len(numbers)):
                    if numbers[i] + curr_sum <= target:
                        dfs(numbers[i:],curr_sum+numbers[i],curr_list + [numbers[i]])
        dfs(candidates,0,[])
        return answear
