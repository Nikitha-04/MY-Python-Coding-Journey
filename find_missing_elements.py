from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)

        s = set(nums)
        ans = []

        for x in range(smallest, largest + 1):
            if x not in s:
                ans.append(x)

        return ans
