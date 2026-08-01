from functools import lru_cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dp(left, right):
            if left == right:
                return nums[left]

            pick_left = nums[left] - dp(left + 1, right)
            pick_right = nums[right] - dp(left, right - 1)

            return max(pick_left, pick_right)

        return dp(0, len(nums) - 1) >= 0
