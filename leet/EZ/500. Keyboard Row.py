class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_dict = {}
        for char in "qwertyuiop":
            keyboard_dict[char] = 1
        for char in "asdfghjkl":
            keyboard_dict[char] = 2
        for char in "zxcvbnm":
            keyboard_dict[char] = 3

        def all_same_row(word,row):
                for char in word:
                    if keyboard_dict[char] != row:
                        return False
                return True
        answear = []

        for word in words:
            lowerword =word.lower()
            if all_same_row(lowerword,keyboard_dict[lowerword[0]]):
                answear.append(word)

        return answear

print(Solution.findWords(Solution,["Hello","Alaska","Dad","Peace"]))