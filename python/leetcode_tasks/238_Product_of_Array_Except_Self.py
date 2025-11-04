import heapq
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)

    prefix = [1 for _ in range(n)]
    suffix = [1 for _ in range(n)]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    result = [prefix[i] * suffix[i] for i, _ in enumerate(nums)]
    return result


if __name__ == "__main__":
    # s = "anagram"
    # t = "nagaram"
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
