# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import self as self


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        rvalue = []
        combinationSumreal(self, candidates, target, [], rvalue)
        return rvalue


def combinationSumreal(self, candidates, target, currlist, rtype):
    for i in range(len(candidates)):
        curnum = candidates[i]
        if (target - curnum == 0):
            currlist.append(curnum)
            rtype.append(currlist)
            break
        if (target - curnum > 0):
            combinationSumreal(self, candidates[i:], target - curnum, currlist + [curnum], rtype)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution.combinationSum(self, [1,5,10, 25], 25))
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
