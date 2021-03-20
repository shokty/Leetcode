class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        sety = set()

        def translate_word(word):
            rval = ""
            for char in word:
                rval += morse[ord(char) - 97]
            return rval
        for word in words:
            sety.add(translate_word(word))
        return len(sety)

print(ord('b')-97)