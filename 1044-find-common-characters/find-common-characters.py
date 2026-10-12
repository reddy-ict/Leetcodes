class Solution(object):
    def commonChars(self, words):
        result = list(words[0])

        for word in words[1:]:
            for char in result[:]:
                if char in word:
                    word = word.replace(char, "", 1)
                else:
                    result.remove(char)

        return result