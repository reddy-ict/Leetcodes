class Solution(object):
    def beautifulArray(self, n):
        def solve(n):
            if n == 1:
                return [1]

            odd = solve((n + 1) // 2)
            even = solve(n // 2)

            return (
                [2 * x - 1 for x in odd] +
                [2 * x for x in even]
            )

        return solve(n)