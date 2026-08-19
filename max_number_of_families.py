class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):

        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            rows.setdefault(row, set()).add(seat)

        answer = (n - len(rows)) * 2

        for seats in rows.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                # We can place two groups
                answer += 2

            elif left or middle or right:
                # We can place one group
                answer += 1

        return answer
