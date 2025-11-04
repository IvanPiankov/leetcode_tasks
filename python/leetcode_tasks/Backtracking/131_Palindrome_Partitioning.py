
from typing import List



class Solution:

    def is_palindrome(self, sub_string: str) -> bool:
        return sub_string == sub_string[::-1]


    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []

        def backtracking(start_idx):
            if start_idx == len(s):
                result.append(temp.copy())
                return

            for idx in range(start_idx, len(s)):
                sub_string = s[start_idx:idx + 1]
                if self.is_palindrome(sub_string):
                    temp.append(sub_string)
                    backtracking(idx + 1)
                    temp.pop()

        backtracking(0)

        return result






if __name__ == "__main__":
    # Test 1
    s = "aab"
    partition = Solution().partition(s)
    print(partition)
    # Test 2
    s = "a"
    partition = Solution().partition(s)
    print(partition)
    # Test 3
    s = "aaab"
    partition = Solution().partition(s)
    print(partition)