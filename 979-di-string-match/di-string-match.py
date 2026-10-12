class Solution(object):
    def diStringMatch(self, s):
        nums = list(range(len(s) + 1))
        result = []

        for ch in s:
            if ch == 'I':
                result.append(nums.pop(0))
            else:
                result.append(nums.pop())

        result.append(nums[0])
        return result