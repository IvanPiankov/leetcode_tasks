

class Solution:

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1

        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1

        return sum(num for row in dp for num in row)



if __name__ == "__main__":
    # Test 1
    s = "abc"
    ans = Solution().countSubstrings(s)
    print(ans)
    # Test 2
    s = "aaa"
    ans = Solution().countSubstrings(s)
    print(ans)
