from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    # Test 1
    s = [1,2,5]
    amount = 11
    ans = Solution().coinChange(coins=s, amount=amount)
    print(ans)
    # Test 2
    s = [2]
    amount = 3
    ans = Solution().coinChange(coins=s, amount=amount)
    print(ans)
    # Test 2
    s = [1]
    amount = 0
    ans = Solution().coinChange(coins=s, amount=amount)
    print(ans)
