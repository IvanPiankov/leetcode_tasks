from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = 0
        for i in range(len(nums)):
            expected_sum += i + 1
        return expected_sum - sum(nums)

if __name__ == "__main__":
    # Test 1
    data_set = [9,6,4,2,3,5,7,0,1]
    subsets = Solution().missingNumber(data_set)
    print(subsets)


