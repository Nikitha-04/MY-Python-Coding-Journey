class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sum for quickly finding range sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score for interval [l, r]
        dp = [[0] * n for _ in range(n)]

        # Consider intervals of increasing length
        for length in range(2, n + 1):

            for l in range(n - length + 1):
                r = l + length - 1

                # Try every possible split
                for k in range(l, r):

                    left_sum = prefix[k + 1] - prefix[l]
                    right_sum = prefix[r + 1] - prefix[k + 1]

                    if left_sum < right_sum:
                        dp[l][r] = max(
                            dp[l][r],
                            left_sum + dp[l][k]
                        )

                    elif left_sum > right_sum:
                        dp[l][r] = max(
                            dp[l][r],
                            right_sum + dp[k + 1][r]
                        )

                    else:
                        dp[l][r] = max(
                            dp[l][r],
                            left_sum + dp[l][k],
                            right_sum + dp[k + 1][r]
                        )

        return dp[0][n - 1]
