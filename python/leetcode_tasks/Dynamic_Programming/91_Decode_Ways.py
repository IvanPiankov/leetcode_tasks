

class Solution:

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            if i >= 2:
                two_digit_value = int(s[i-2: i])
                if 10 <= two_digit_value <= 26:
                    dp[i] += dp[i-2]

        return dp[n]


if __name__ == "__main__":
    # Test 1
    # s = "12"
    # ans = Solution().numDecodings(s)
    # print(ans)
    # # Test 2
    # s = "226"
    # ans = Solution().numDecodings(s)
    # print(ans)
    # Test 3
    s = "060"
    ans = Solution().numDecodings(s)
    print(ans)
