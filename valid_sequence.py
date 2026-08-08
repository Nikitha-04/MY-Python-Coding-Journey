from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # suf[i] = smallest index in word1 from which
        # word2[i:] can be matched exactly.
        suf = [-1] * (m + 1)

        pos = n - 1

        suf[m] = n

        for j in range(m - 1, -1, -1):
            while pos >= 0 and word1[pos] != word2[j]:
                pos -= 1

            if pos < 0:
                break

            suf[j] = pos
            pos -= 1

        ans = []
        j = 0
        prev = -1
        used_mismatch = False

        for i in range(n):
            if j == m:
                break

            # Option 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
                continue

            # Option 2: use our one mismatch
            if not used_mismatch:
                # After selecting i, word2[j+1:] must be
                # exactly matchable after i.
                if j + 1 == m or (
                    suf[j + 1] != -1 and suf[j + 1] > i
                ):
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        if j == m:
            return ans

        return []
