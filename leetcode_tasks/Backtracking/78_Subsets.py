# Definition for singly-linked list.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        cur = []
        def backtracking(idx: int) -> None:
            if idx >= len(nums):
                return result.append(cur.copy())

            cur.append(nums[idx])
            backtracking(idx + 1)

            cur.pop()
            backtracking(idx + 1)

        backtracking(0)
        return result







if __name__ == "__main__":
    # Test 1
    data_set = [1,2,3]
    subsets = Solution().subsets(data_set)
    print(subsets)


