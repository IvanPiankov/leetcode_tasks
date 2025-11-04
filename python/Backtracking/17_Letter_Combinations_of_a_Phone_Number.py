
from typing import List



class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        temp = ""

        def backtracking(idx, temp):
            if len(temp) == len(digits):
                result.append(temp[:])
                return

            for letter in digit_to_letters[digits[idx]]:
                backtracking(idx + 1, temp + letter)

        backtracking(0, temp)

        return result






if __name__ == "__main__":
    # Test 1
    digits = "23"
    partition = Solution().letterCombinations(digits)
    print(partition)
    # Test 2
    digits = ""
    partition = Solution().letterCombinations(digits)
    print(partition)
    # Test 3
    digits = "2"
    partition = Solution().letterCombinations(digits)
    print(partition)