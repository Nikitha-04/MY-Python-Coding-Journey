class Solution {
public:

    long long gcd(long long a, long long b) {
        while (b != 0) {
            long long temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    long long lcm(long long a, long long b) {
        return a / gcd(a, b) * b;
    }

    // Number of valid amounts <= x
    long long count(long long x, vector<int>& coins) {

        int n = coins.size();
        long long ans = 0;

        // Try every subset of coins
        for (int mask = 1; mask < (1 << n); mask++) {

            long long L = 1;
            int bits = 0;
            bool valid = true;

            for (int i = 0; i < n; i++) {

                if (mask & (1 << i)) {

                    bits++;

                    L = lcm(L, coins[i]);

                    // No multiple of L can be <= x
                    if (L > x) {
                        valid = false;
                        break;
                    }
                }
            }

            if (!valid)
                continue;

            long long ways = x / L;

            if (bits % 2 == 1)
                ans += ways;
            else
                ans -= ways;
        }

        return ans;
    }

    long long findKthSmallest(vector<int>& coins, int k) {

        long long mn = *min_element(coins.begin(), coins.end());

        long long low = 1;
        long long high = mn * (long long)k;

        while (low < high) {

            long long mid = low + (high - low) / 2;

            if (count(mid, coins) >= k) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }

        return low;
    }
};
