class Solution:
    def almostMissing(self, nums, k):
        count = [0] * 51

        # Check every subarray of size k
        for i in range(len(nums) - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            # Each distinct number appears in this subarray
            for x in seen:
                count[x] += 1

        # Find the largest number appearing in exactly one subarray
        for x in range(50, -1, -1):
            if count[x] == 1:
                return x

        return -1
