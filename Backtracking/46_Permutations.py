
from typing import List



class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start_idx):
            if start_idx == len(nums):
                result.append(nums.copy())
                return

            for idx in range(start_idx, len(nums)):
                nums[start_idx], nums[idx] = nums[idx], nums[start_idx]
                backtracking(start_idx + 1)
                nums[start_idx], nums[idx] = nums[idx], nums[start_idx]

        backtracking(0)

        return result






if __name__ == "__main__":
    # Test 1
    nums = [1,2,3]
    permutate = Solution().permute(nums)
    print(permutate)
    # Test 2
    nums = [0,1]
    permutate = Solution().permute(nums)
    print(permutate)
    # Test 3
    nums = [1]
    permutate = Solution().permute(nums)
    print(permutate)