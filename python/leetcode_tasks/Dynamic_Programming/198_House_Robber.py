
from typing import List



class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1 = nums[0]
        prev2 = max(nums[1], prev1)

        for i in range(2, len(nums)):
            curr = max(prev1 + nums[i], prev2)
            prev1, prev2 = prev2, curr

        return max(prev1, prev2)


if __name__ == "__main__":
    # Test 1
    # nums = [1,2,3,1]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # # Test 2
    # nums = [2,7,9,3,1]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # Test 2
    nums = [2,1,1,2]
    robbed = Solution().rob(nums)
    print(Solution.__dict__)
    print(robbed)