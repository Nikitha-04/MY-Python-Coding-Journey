from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        # Each node:
        # [left_char, right_char, left_len, right_len, best, length]
        tree = [None] * (4 * n)

        def build(node, start, end):
            if start == end:
                tree[node] = [
                    s[start],  # left_char
                    s[start],  # right_char
                    1,         # left_len
                    1,         # right_len
                    1,         # best
                    1          # length
                ]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def merge(left, right):
            if left is None:
                return right

            if right is None:
                return left

            left_char, _, left_len, left_right_len, left_best, left_size = left
            _, right_char, right_left_len, right_len, right_best, right_size = right

            total_len = left_size + right_size

            # Start with the best answer from either side
            best = max(left_best, right_best)

            # If the boundary characters are equal,
            # the suffix of left + prefix of right form
            # one repeating substring.
            if left[1] == right[0]:
                best = max(
                    best,
                    left_right_len + right_left_len
                )

            # Calculate prefix length
            new_left_len = left_len

            if left_len == left_size and left[1] == right[0]:
                new_left_len = left_size + right_left_len

            # Calculate suffix length
            new_right_len = right_len

            if right_len == right_size and left[1] == right[0]:
                new_right_len = right_size + left_right_len

            return [
                left_char,
                right_char,
                new_left_len,
                new_right_len,
                best,
                total_len
            ]

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build the initial segment tree
        build(1, 0, n - 1)

        result = []

        # Process each query
        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)

            # tree[1][4] = best
            result.append(tree[1][4])

        return result
