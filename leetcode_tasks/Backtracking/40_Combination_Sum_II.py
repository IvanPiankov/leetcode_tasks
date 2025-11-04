# Definition for singly-linked list.
from typing import List




class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtracking(target, idx, current):
            if target < 0:
                return
            elif target == 0:
                result.append(current)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtracking(target - candidates[i], i+1, current + [candidates[i]])

        backtracking(target, 0, [])

        return result






if __name__ == "__main__":
    # Test 1
    candidates = [10,1,2,7,6,1,5]
    target = 8
    subsets = Solution().combinationSum2(candidates, target)
    print(subsets)