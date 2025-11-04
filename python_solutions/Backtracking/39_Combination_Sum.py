# Definition for singly-linked list.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        current = []

        def backtracking(idx, current):
            if sum(current) == target:
                return result.append(current.copy())

            if sum(current) > target or idx >= len(candidates):
                return

            current.append(candidates[idx])
            backtracking(idx, current)

            current.pop()
            backtracking(idx + 1, current)

        backtracking(0, current)

        return result







if __name__ == "__main__":
    # Test 1
    candidates = [2,3,6,7]
    target = 7
    subsets = Solution().combinationSum(candidates, target)
    print(subsets)