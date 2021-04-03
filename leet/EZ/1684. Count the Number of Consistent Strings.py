class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        counter = 0
        for word in words:
            add_to_counter = True
            for char in word:
                if char not in allowed and add_to_counter:
                    add_to_counter = False
            if add_to_counter:
                counter +=1
        return counter

print(Solution.countConsistentStrings(Solution,"ab",["ad","bd","aaab","baa","badab"]))