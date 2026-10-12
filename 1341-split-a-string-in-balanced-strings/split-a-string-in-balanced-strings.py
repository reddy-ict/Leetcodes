class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        result = 0

        for ch in s:
            if ch == 'R':
                count += 1
            else:
                count -= 1

            if count == 0:
                result += 1

        return result