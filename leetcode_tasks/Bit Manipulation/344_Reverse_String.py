from typing import List


class Solution:
    def __init__(self):
        self.counter = 0

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l +=1
            r -=1




if __name__ == "__main__":
    # Test 1
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    print(f"Test 1- {s}")
    # Test 2
    s = ["H","a","n","n","a","h"]
    Solution().reverseString(s)
    print(f"Test 2- {s}")
    # Test 3
    s = ["H"]
    Solution().reverseString(s)
    print(f"Test 3- {s}")


