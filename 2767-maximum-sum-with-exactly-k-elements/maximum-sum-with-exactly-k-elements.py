class Solution(object):
    def maximizeSum(self, nums, k):
        maximum = max(nums)
        score = 0

        for i in range(k):
            score += maximum
            maximum += 1

        return score