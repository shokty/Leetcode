"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        dicty = {}
        for employee in employees:
            dicty[employee[0]] = employee[1:]
        Q = deque()
        Q.append(id)
        value = 0
        while Q:
            curr = dicty[Q.pop()]
            value += curr[0]
            for subemp in curr[1]:
                Q.append(subemp)

        return value

e = [[1,2,[2]], [2,3,[]]]
print(Solution.getImportance(Solution,e,2))