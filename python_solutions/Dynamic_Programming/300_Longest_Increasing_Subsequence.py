
from typing import List



class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * (len(nums) + 1)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)



if __name__ == "__main__":
    # # Test 1
    nums = [10,9,2,5,3,7,101,18]
    answer = Solution().lengthOfLIS(nums)
    print(answer)
    # Test 2
    nums = [0,1,0,3,2,3]
    answer = Solution().lengthOfLIS(nums)
    print(answer)
    # Test 3
    nums = [7,7,7,7,7,7,7]
    answer = Solution().lengthOfLIS(nums)
    print(answer)