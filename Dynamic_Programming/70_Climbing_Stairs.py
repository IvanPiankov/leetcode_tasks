
from typing import List



class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        previous, current = 1, 2

        for _ in range(2, n):
            temp = current
            current = previous + current
            previous = temp

        return current







if __name__ == "__main__":
    # Test 1
    n = 2
    partition = Solution().climbStairs(n)
    print(partition)
    # Test 2
    n = 3
    partition = Solution().climbStairs(n)
    print(partition)
    # Test 2
    n = 4
    partition = Solution().climbStairs(n)
    print(partition)
    # Test 2
    n = 5
    partition = Solution().climbStairs(n)
    print(partition)