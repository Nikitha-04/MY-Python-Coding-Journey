class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        zero = cnt[0]
        one = cnt[1]
        two = cnt[2]

        if one == 0 and two == 0:
            return False

        if one == 0:
            return two > 2 and zero % 2 == 1

        if two == 0:
            return one > 2 and zero % 2 == 1

        if zero % 2 == 0:
            return True

        return abs(one - two) > 2
