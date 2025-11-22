
from typing import List



class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)] == True:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]



if __name__ == "__main__":
    # # Test 1
    s = "leetcode"
    wordDict = ["leet", "code"]
    answer = Solution().wordBreak(s, wordDict)
    print(answer)
    # # # Test 2
    # nums = [1,2,3,1]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # # Test 2
    # nums = [1,2,3]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # Test 3
    # nums = [0]
    # robbed = Solution().rob(nums)
    # print(robbed)