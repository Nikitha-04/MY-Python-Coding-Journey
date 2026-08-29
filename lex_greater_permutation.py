class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Try making the answer greater at position i.
        # We keep target[0:i] equal to target.
        for i in range(n - 1, -1, -1):

            # Copy the frequency array
            remaining = count[:]

            # Try to match target[0:i]
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # At position i, choose the smallest character
            # strictly greater than target[i].
            target_idx = ord(target[i]) - ord('a')

            for c in range(target_idx + 1, 26):
                if remaining[c] > 0:

                    # We found the first character that makes
                    # our string strictly greater.

                    answer = target[:i] + chr(c + ord('a'))

                    # Put all remaining characters in sorted order
                    remaining[c] -= 1

                    suffix = []

                    for k in range(26):
                        suffix.append(chr(k + ord('a')) * remaining[k])

                    return answer + ''.join(suffix)

        return ""
