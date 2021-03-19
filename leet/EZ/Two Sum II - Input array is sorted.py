class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while (start < end):
            if (numbers[end] + numbers[start] == target):
                return [start+1,end+1]
            elif (numbers[end] + numbers[start] > target):
                end -= 1
            else:
                start +=1

        return -1
numbers = [2,7,11,15]
target = 9
print(Solution.twoSum(Solution,numbers,target))

