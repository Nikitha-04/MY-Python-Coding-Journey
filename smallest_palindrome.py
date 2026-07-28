from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        first_half = []
        middle = ""

        for ch in sorted(count.keys()):
            first_half.append(ch * (count[ch] // 2))
            if count[ch] % 2 == 1:
                middle = ch

        first_half = "".join(first_half)
        return first_half + middle + first_half[::-1]
