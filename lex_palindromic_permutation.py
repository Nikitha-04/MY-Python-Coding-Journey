class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether a palindromic permutation is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Build counts for the first half
        half_count = [0] * 26

        for i in range(26):
            half_count[i] = count[i] // 2

        half_len = n // 2

        # Helper to construct the palindrome from its first half
        def make_palindrome(half):
            if n % 2 == 1:
                return half + middle + half[::-1]
            else:
                return half + half[::-1]

        # We need the smallest first half that produces
        # a palindrome strictly greater than target.
        #
        # Since palindrome comparison is determined by the
        # first half (and possibly the middle character),
        # we can find the smallest half greater than target's
        # first half.

        target_half = target[:half_len]

        # First try to construct a half equal to target_half.
        # If the resulting palindrome is already > target,
        # it is the answer.
        remaining = half_count[:]
        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            palindrome = make_palindrome(target_half)

            if palindrome > target:
                return palindrome

        # We need to find the smallest half that is greater
        # than target_half.
        #
        # Try changing the half from right to left.
        for i in range(half_len - 1, -1, -1):

            remaining = half_count[:]

            # Match target_half[0:i]
            possible = True

            for j in range(i):
                idx = ord(target_half[j]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # At position i, choose the smallest character
            # greater than target_half[i].
            current = ord(target_half[i]) - ord('a')

            for c in range(current + 1, 26):

                if remaining[c] > 0:

                    # Use this character
                    remaining[c] -= 1

                    # Put all remaining characters in sorted order
                    suffix = []

                    for k in range(26):
                        suffix.append(
                            chr(k + ord('a')) * remaining[k]
                        )

                    new_half = (
                        target_half[:i]
                        + chr(c + ord('a'))
                        + ''.join(suffix)
                    )

                    return make_palindrome(new_half)

        return 
