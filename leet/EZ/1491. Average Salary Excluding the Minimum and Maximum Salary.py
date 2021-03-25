class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sum = 0.0
        mx = 0
        mn = float('inf')
        for kasaf in salary:
            sum += kasaf
            mx = max(mx,kasaf)
            mn = min(mn,kasaf)
        return (sum - mn - mx)/(len(salary)-2)

print(Solution.average(Solution,[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))