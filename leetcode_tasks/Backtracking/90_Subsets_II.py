from typing import List

class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        curr = []

        def backtracking(start_idx, curr) -> None:
            result.append(curr.copy())

            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, curr)
        return result







if __name__ == "__main__":
    # Test 1
    nums = [1,2,2]
    subsets = Solution().subsetsWithDup(nums)
    print(subsets)


