class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = [0] * n

        start = 0

        while start < n:
            end = start

            # Find one connected component.
            while (
                end + 1 < n
                and arr[end + 1][0] - arr[end][0] <= limit
            ):
                end += 1

            # Values in this group
            values = []

            # Original indices in this group
            indices = []

            for k in range(start, end + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # To get lexicographically smallest result:
            # smallest values go to smallest indices.
            indices.sort()

            for value, index in zip(values, indices):
                ans[index] = value

            start = end + 1

        return ans
