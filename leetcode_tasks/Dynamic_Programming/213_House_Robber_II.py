
from typing import List



class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def get_max_sum(short_nums) -> int:
            if len(short_nums) == 1:
                return short_nums[0]

            prev1 = short_nums[0]
            prev2 = max(short_nums[1], prev1)

            for i in range(2, len(short_nums)):
                curr = max(prev1 + short_nums[i], prev2)
                prev1, prev2 = prev2, curr

            return max(prev1, prev2)

        return max(get_max_sum(nums[:-1]), get_max_sum(nums[1::]))


if __name__ == "__main__":
    # # Test 1
    # nums =  [2,3,2]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # # # Test 2
    # nums = [1,2,3,1]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # # Test 2
    # nums = [1,2,3]
    # robbed = Solution().rob(nums)
    # print(robbed)
    # Test 3
    nums = [0]
    robbed = Solution().rob(nums)
    print(robbed)