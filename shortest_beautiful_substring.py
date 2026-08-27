class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        min_len = float('inf')
        answer = ""

        for i in range(n):
            ones = 0

            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    current = s[i:j + 1]

                    if len(current) < min_len:
                        min_len = len(current)
                        answer = current

                    elif len(current) == min_len:
                        answer = min(answer, current)

                    # Adding more characters can only increase length
                    break

        return answer
