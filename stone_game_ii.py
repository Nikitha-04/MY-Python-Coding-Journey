from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with M
        memo = {}

        def dp(i, M):
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                opponent = dp(i + X, max(M, X))
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)
