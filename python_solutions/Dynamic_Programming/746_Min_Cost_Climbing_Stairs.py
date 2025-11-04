
from typing import List



class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)

        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])


    def minCostClimbingStairsSecond(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        prev1 = cost[0]
        prev2 = cost[1]

        for i in range(2, n):
            curr = min(prev1, prev2) + cost[i]
            prev1, prev2 = prev2, curr

        return min(prev1, prev2)



if __name__ == "__main__":
    # Test 1
    cost = [10,15,20]
    min_cost = Solution().minCostClimbingStairsSecond(cost)
    print(min_cost)
    # Test 2
    cost = [1,100,1,1,1,100,1,1,100,1]
    min_cost = Solution().minCostClimbingStairsSecond(cost)
    print(min_cost)